import os
import time

from dj_experiment.tasks.tasks import longtime_add, netcdf_save
from example.settings import DJ_EXPERIMENT_BASE_DATA_DIR

if __name__ == '__main__':
    result = longtime_add.delay(1, 2)
    # at this time, our task is not finished, so it will return False
    print 'Task finished? ', result.ready()
    print 'Task result: ', result.result
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print 'Task finished? ', result.ready()
    print 'Task result: ', result.result

    rcmdatadir = DJ_EXPERIMENT_BASE_DATA_DIR
    result1 = netcdf_save.delay(14, rcmdatadir)
    print 'Task netcdf finished? ', result1.ready()
    print 'Task result1: ', result1.result
    time.sleep(10)
    print 'Task netcdf finished? ', result1.ready()
    print 'Task result1: ', result1.result
