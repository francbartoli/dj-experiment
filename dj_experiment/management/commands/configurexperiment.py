import logging
import os

from dj_experiment.models import Case as CaseModel
from dj_experiment.models import Experiment as ExperimentModel
from dj_experiment.models import FieldGroup as FieldGroupModel
from dj_experiment.models import Value as ValueModel
from django.core.management.base import BaseCommand, CommandError
from experiment import Case, Experiment, Field


class Command(BaseCommand):
    """Obtain an experiment configured from the catalog."""

    help = 'Obtain an experiment configured from the catalog'

    # def __init__(self):
    #     """Call the BaseCommand constructor."""
    #     super(Command, self).__init__()
    #     self.style = color_style()

    def add_arguments(self, parser):
        """Add arguments for handling the command."""
        # Named (optional) arguments start with --
        parser.add_argument('-e', '--experiment',  # argument flag
                            dest='experiment',  # argument name
                            default=None,
                            help='Create the configuration of an experiment',
                            )
        parser.add_argument('-b', '--basepath',  # argument flag
                            dest='basepath',  # argument name
                            default=None,
                            help='Create the configuration of an experiment in \
                            a specific base path',
                            )
        parser.add_argument('-x', '--export',  # argument flag
                            dest='export',  # argument name
                            default=None,
                            help='Return the configuration of an experiment in \
                            a specific base path',
                            )

    def handle(self, *args, **options):
        """Obtain an experiment configured from the catalog."""
        if not (options.get('experiment') and options.get('basepath')):
            raise CommandError(
                "configurexperiment wants at least one named argument"
            )
        else:
            experiment_name = options['experiment']
            experiment_basepath = options.get('basepath')
            if options.get('export'):
                experiment_return = options.get('export')
            else:
                experiment_return = False

        def _load_cases(self, expname):
            """."""
            caselist = list()
            try:
                casevals = [
                    exp.cases.values(
                    ) for exp in ExperimentModel.objects.filter(
                        name=expname
                    )
                ]
            except ExperimentModel.DoesNotExist:
                raise CommandError('Experiment "%s" does not exist' % expname)

            for caseval in casevals[0]:
                shortname = caseval.get("shortname")
                longname = caseval.get("longname")
                try:
                    valslist = [
                        case.casevals.values(
                        ) for case in CaseModel.objects.filter(
                            name=caseval.get("name")
                        )
                    ]
                except CaseModel.DoesNotExist:
                    raise CommandError(
                        'Case "%s" does not exist' % caseval.get("name")
                    )
                vals = [val.get("val") for val in valslist[0]]
                caselist.append(Case(shortname,
                                     longname,
                                     vals))

            return caselist

        def _load_fieldgroups(self, expname):
            """."""
            fieldgrouplist = list()
            try:
                for exp in ExperimentModel.objects.filter(name=expname):
                    fg_pk = exp.fieldgroups_id
            except ExperimentModel.DoesNotExist:
                raise CommandError('Experiment "%s" does not exist' % expname)
            try:
                fieldgroup = FieldGroupModel.objects.filter(
                    pk=fg_pk
                ).iterator()
                for fieldgroupitem in fieldgroup:
                    shortname = fieldgroupitem.shortname
                    longname = fieldgroupitem.longname
                    initialposition = fieldgroupitem.is_initialposition
                    try:
                        fieldnames = [
                            value.val for value in ValueModel.objects.filter(
                                fieldgroups=fg_pk
                            )
                        ]
                    except ValueModel.DoesNotExist:
                        raise CommandError(
                            'ValueModel with fieldgroups id "%s" \
                             does not exist' % fg_pk)
                    fieldgrouplist.append(Field(shortname,
                                                longname,
                                                fieldnames,
                                                initialposition))
            except FieldGroupModel.DoesNotExist:
                raise CommandError('FieldGroup id "%s" does not exist' % fg_pk)
            return fieldgrouplist

        def _load_timeseries(self, expname):
            """."""
            vals = ExperimentModel.objects.filter(name=expname).values()
            for val in vals.iterator():
                timeseriesval = val.get("timeseries")
            return timeseriesval

        def _load_datadir(self, expname):
            """."""
            vals = ExperimentModel.objects.filter(name=expname).values()
            for val in vals.iterator():
                datadirval = val.get("data_dir")
            return datadirval

        def _load_casepath(self, expname):
            """."""
            vals = ExperimentModel.objects.filter(name=expname).values()
            for val in vals.iterator():
                casepathval = val.get("case_path")
            return casepathval

        def _load_initialposition(self, expname):
            """."""
            vals = ExperimentModel.objects.filter(name=expname).values()
            for val in vals.iterator():
                initialpositionval = val.get("initial_position")
            return initialpositionval

        def _load_outputprefix(self, expname):
            """."""
            vals = ExperimentModel.objects.filter(name=expname).values()
            for val in vals.iterator():
                outputprefixval = val.get("output_prefix")
            return outputprefixval

        def _load_outputsuffix(self, expname):
            """."""
            vals = ExperimentModel.objects.filter(name=expname).values()
            for val in vals.iterator():
                outputsuffixval = val.get("output_suffix")
            return outputsuffixval

        def _load_validatedata(self, expname):
            """."""
            vals = ExperimentModel.objects.filter(name=expname).values()
            for val in vals.iterator():
                validatedataval = val.get("validate_data")
            return validatedataval

        _BASE_DIR = experiment_basepath
        xperiment = Experiment(
            experiment_name,
            cases=_load_cases(self, experiment_name),
            fieldgroups=_load_fieldgroups(self, experiment_name),
            timeseries=_load_timeseries(self, experiment_name),
            data_dir=os.path.join(_BASE_DIR,
                                  _load_datadir(self, experiment_name)),
            case_path=_load_casepath(self, experiment_name),
            initial_position=_load_initialposition(self, experiment_name),
            output_prefix=_load_outputprefix(self, experiment_name),
            output_suffix=_load_outputsuffix(self, experiment_name),
            validate_data=_load_validatedata(self, experiment_name)
        )

        if experiment_return:
            self.stdout.ending = ''
            self.stdout.write(xperiment.to_dict())
            logging.debug(xperiment.to_dict())
            return xperiment.to_dict()
            # self.stdout.write(self.style.NOTICE(
            #     'Successfully returned configuration \
            #     for "%s"' % experiment_name))
            logging.info('Successfully returned configuration \
                for "%s"' % experiment_name)
        self.stdout.write(self.style.NOTICE(
            'Successfully created configuration for "%s"' % experiment_name))

        logging.info('Command executed successfully!')
