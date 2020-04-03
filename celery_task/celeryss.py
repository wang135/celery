from celery import Celery
# from celery_task.task1 import test_celery
# from celery_task.task2 import test_celery2
import time
# 立即告知celery去执行test_celery任务，并传入一个参数

cel = Celery('celeryss',
             broker='redis://127.0.0.1:6379/4',
             backend='redis://127.0.0.1:6379/5',
             # # 包含以下两个任务文件，去相应的py文件中找任务，对多个任务做分类
             # include=['celery_task.tasks1',
             #          'celery_task.tasks2'
             #          ]
             )

@cel.task
def test_celery(res):
    time.sleep(5)
    return ("test_celery任务结果:%s"%res)
# 时区
cel.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
cel.conf.enable_utc = False