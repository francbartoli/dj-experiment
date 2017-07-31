=============================
Experiment
=============================

.. image:: https://badge.fury.io/py/dj-experiment.svg
    :target: https://badge.fury.io/py/dj-experiment

.. image:: https://travis-ci.org/francbartoli/dj-experiment.svg?branch=master
    :target: https://travis-ci.org/francbartoli/dj-experiment

.. image:: https://codecov.io/gh/francbartoli/dj-experiment/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/francbartoli/dj-experiment

Django application for organizing numerical model experiment output

Documentation
-------------

The full documentation is at https://dj-experiment.readthedocs.io.

Quickstart
----------

Install Experiment::

    pip install dj-experiment

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_experiment.apps.DjExperimentConfig',
        ...
    )

Add Experiment's URL patterns:

.. code-block:: python

    from dj_experiment import urls as dj_experiment_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_experiment_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
