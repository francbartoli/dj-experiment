from dj_experiment.models import Catalog
from django.core.management.base import BaseCommand, CommandError
from humanfriendly.tables import format_smart_table


class Command(BaseCommand):
    """Retrieve the list of experiments from a catalog."""

    help = 'Retrieve the list of experiments from a catalog'

    def add_arguments(self, parser):
        """Add arguments for handling the command."""
        # Named (optional) arguments start with --
        parser.add_argument('-C', '--catalog',  # argument flag
                            dest='catalog',  # argument name
                            default=None,
                            help='Query catalog by its name',
                            )

    def handle(self, *args, **options):
        """List all the entries from a catalog name."""
        if not options.get('catalog'):
            raise CommandError(
                "listexperimentsbycatalog wants at least one named argument"
            )
        else:
            catalog_name = options['catalog']
        column_names = ['Experiment Name']

        experiments = (
            cat.xperiments.values('name')
            for cat in Catalog.objects.filter(
                name=catalog_name
            )
        )
        explist = list()
        for xperiment in experiments:
            for exp_kws in xperiment:
                explist.append([exp_kws['name'], ])

        self.stdout.write(format_smart_table(
            explist, column_names))
