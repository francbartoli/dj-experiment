import ast
import logging
import os
import sys
from StringIO import StringIO

import scandir
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


def get_files(inst, datadir):

    extension = inst.output_suffix
    return _build_fullfilepathname(extension, datadir)


def get_keywords(inst, filetuple):

    # catch year as extra_keywords and clean it
    searchfile = filetuple[0]
    logging.debug("Search keywords for file %s" % searchfile)
    fields = inst.get_fieldgroup_vals(inst.fieldgroups[0])[0]
    cleanfile, extra_keywords = _build_extrakeywords(searchfile,
                                                     inst.all_case_vals(),
                                                     fields,
                                                     inst.output_suffix)
    logging.debug("Cleaned file ===> %s" % cleanfile)
    searchcleanedfile = os.path.join(settings.DJ_EXPERIMENT_DATA_DIR,
                                     str(filetuple[3]),
                                     str(cleanfile))
    logging.debug("Searching for matching cases \
                  with this file ===> %s" % searchcleanedfile)
    filetuple += (searchcleanedfile, )
    fieldcaselist = inst.get_cases_fromfile(searchcleanedfile)
    try:
        matchdict = [
            ({inst.fieldgroups[0]:field},
             matchcases[0]
             ) for field, matchcases in fieldcaselist if matchcases
        ]
        logging.debug(
            "Key/value dictionary of matched cases is ===> %s" % matchdict
        )
        case_keywords = matchdict[0][1].values()
        logging.debug("Case keywords from file %s" % case_keywords)
        logging.debug("Extra keywords from file %s" % extra_keywords)
        keywords = case_keywords + extra_keywords
        if keywords:
            keywords = list(set(keywords))
            logging.info(
                "Final return \nKEYWORDS===>%s\nfrom\nFILE===>%s " % (
                    keywords, filetuple[0])
            )
            return filetuple, keywords, matchdict[0]
    except IndexError as e:
        logging.error(
            "Passed file %s doesn't match any case" % searchcleanedfile
        )
        logging.debug("Exception is %s" % e)
        logging.error(
            "Not able to retrieve any keyword for file %s" % filetuple[0]
        )
        return filetuple, {}, ()


def _build_fullfilepathname(ext, root):

    ext = ext.lower()
    tpl = tuple()

    for dirname, dirs, files in scandir.walk(root):
        for file_ in files:
            if file_.lower().endswith(ext):
                logging.debug("file_=%s" % file_)
                logging.debug("dirname=%s" % dirname)
                logging.debug("fullname=%s" % os.path.join(dirname, file_))
                logging.debug("relpath=%s" % os.path.relpath(dirname, root))
                tpl += ((file_,
                         dirname,
                         os.path.join(dirname, file_),
                         os.path.relpath(dirname, root)), )
    return tpl


def _build_extrakeywords(fn, casevals, fieldvals, filesuffix):

    foundwords = list()
    extrawords = list()

    # find words not present along cases
    words = os.path.splitext(str(fn))[0].split(
        settings.DJ_EXPERIMENT_SEPARATOR
    )
    logging.debug("Input words are ===> %s" % words)
    for word in words:
        if any(
            word in s for s in [
                val for vals in casevals for val in vals
            ]
        ):
            foundwords.append(word)
            logging.debug("Foundwords are ===> %s" % foundwords)
    extrawords = [item for item in words if item not in foundwords]
    logging.debug("Extrawords are ===> %s" % extrawords)
    cleanextrawords = [
        cleanextra for cleanextra in extrawords if cleanextra not in fieldvals
    ]
    logging.debug("Cleanextrawords are ===> %s" % cleanextrawords)
    cleanwords = [clean for clean in words if clean not in cleanextrawords]
    cleanwords.append(filesuffix)
    logging.debug("Cleanwords are ===> %s" % cleanwords)
    fn = settings.DJ_EXPERIMENT_SEPARATOR.join(cleanwords)
    logging.debug("Clean content of fn is ===> %s" % fn)
    extrawords = map(unicode, extrawords)
    return fn, extrawords
