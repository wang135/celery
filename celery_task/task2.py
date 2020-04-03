import time
from celery_task.celeryss import cel
@cel.task
def test_celery2(res):
    time.sleep(10)
    return ("test_celery2任务结果:%s"%res)
