from celery.result import AsyncResult
from celery_task.celeryss import cel


async1= AsyncResult(id="08eb2778-24e1-44e4-a54b-56990b3519ef", app=cel)

if async1.successful():
    result = async1.get()
    print(result)
    # result.forget() # 将结果删除,执行完成，结果不会自动删除
    # async.revoke(terminate=True)  # 无论现在是什么时候，都要终止
    # async.revoke(terminate=False) # 如果任务还没有开始执行呢，那么就可以终止。
elif async1.failed():
    print('执行失败')
elif async1.status == 'PENDING':
    print('任务等待中被执行')
elif async1.status == 'RETRY':
    print('任务异常后正在重试')
elif async1.status == 'STARTED':
    print('任务已经开始被执行')
