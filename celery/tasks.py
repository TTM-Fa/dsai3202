# from celery import Celery
# # Configure Celery to use RabbitMQ
# # as the message broker
# app = Celery('tasks',
#              broker='pyamqp://guest@localhost//')

from celery import Celery

# app = Celery('tasks', broker='pyamqp://guest@localhost//', 
#              backend='redis://localhost')
app = Celery('tasks',
             broker='redis://10.102.10.80:6379/0',
             backend='redis://10.102.10.80:6379/1')
@app.task
def power(n, power):
    return n ** power

@app.task
def is_prime(n):
    if n < 2:
        return None
    for i in range(2, n):
        if n % i == 0:
            return None
    return n