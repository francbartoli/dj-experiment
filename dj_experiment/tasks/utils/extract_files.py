import ast
import logging
import os
import sys
from StringIO import StringIO

from dj_experiment.conf import settings
from dj_experiment.management.commands.configurexperiment import \
    Command as ConfigureExperiment
from experiment import Case, Experiment, Field


def get_experiment(namedexp, rootdirexp):

    # set default root data dir if passed directory doesn't exist
    if not os.path.exists(rootdirexp):
        logging.debug("Input root directory %s doesn't exist, default \
                value %s" % (rootdirexp, settings.DJ_EXPERIMENT_BASE_DATA_DIR))
        rootdirexp = settings.DJ_EXPERIMENT_BASE_DATA_DIR

    old_stdout = sys.stdout
    # This variable will store everything that is sent to the
    # standard output
    cmd = StringIO()
    sys.stdout = cmd

    # Here we can call anything we like, like external modules,
    # and everything that they will send to standard output will be
    # stored on "cmd"
    ce = ConfigureExperiment()
    ce.handle(experiment=namedexp,
              basepath=rootdirexp,
              export=True)

    # Redirect again the std output to screen
    sys.stdout = old_stdout
    xperkwargs = ast.literal_eval(cmd.getvalue())
    logging.debug("xperkwargs======>%s" % xperkwargs)

    # Try to instantiate cases
    logging.debug("Reading cases")
    try:
        caseitems = xperkwargs['cases'].items()
    except TypeError as e:
        raise ValueError(
            "Couldn't retrieve `caseitems` \
            because `xperkwargs` ===> %s" % xperkwargs)
        logging.debug("Exception is %s" % e)
    cases = []
    for case_short, case_kws in caseitems:
        logging.debug("      {}: {}".format(case_short, case_kws))
        cases.append(Case(case_short, **case_kws))
    xperkwargs['cases'] = cases

    # Try to instantiate fieldgroups
    logging.debug("Reading fieldgroup")
    fieldgroups = []
    for fieldgroup_short, fieldgroup_kws in xperkwargs['fieldgroups'].items():
        logging.debug("      {}: {}".format(fieldgroup_short, fieldgroup_kws))
        fieldgroups.append(Field(fieldgroup_short, **fieldgroup_kws))
    xperkwargs['fieldgroups'] = fieldgroups

    # Create and return the Experiment
    xperiment = Experiment(**xperkwargs)
    logging.debug(xperiment.to_dict())
    return xperiment
