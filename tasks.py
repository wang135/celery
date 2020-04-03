from celery import Celery

app = Celery('tasks', broker='redis://127.0.0.1:6379/8',
             backend='redis://127.0.0.1:6379/9',)

@app.task
def add(x, y):
    return x + y

r = add.delay(2,88)
print(r.result)