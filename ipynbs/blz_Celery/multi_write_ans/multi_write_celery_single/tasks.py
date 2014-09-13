from __future__ import absolute_import
from celery import Celery

app = Celery(
	'multi_write_celery_single',
    broker='mongodb://220.133.188.246',
    backend='mongodb://220.133.188.246',
    include=['tasks']
)

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES = 3600,
)

if __name__ == '__main__':
    app.start()

@app.task
def multi_write(path, content):
    with open(path, "w") as wf:
        wf.write(content)