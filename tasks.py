from celery import Celery

app = Celery('tasks', broker='amqp:psaviuk@localhost//')

@app.task
def add(x, y):
    return x + y
