=====
Usage
=====

To use Experiment in a project, add it to your `INSTALLED_APPS`:

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
