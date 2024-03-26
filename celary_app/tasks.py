from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//', backend='redis://localhost')

@app.task
def power(n, power):
    return n ** power