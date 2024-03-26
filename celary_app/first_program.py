from celery import Celery 

app = Celery("celery_app",
             broker="amqp://guest:guest@localhost",
             backend="rpc://")