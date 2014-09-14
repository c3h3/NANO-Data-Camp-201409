from __future__ import absolute_import
from celery import Celery

app = Celery(
	'multi_write_celery',
    broker='mongodb://140.116.21.177',
    backend='mongodb://140.116.21.177',
    include=['multi_write_celery.tasks']
)

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES = 3600,
)

if __name__ == '__main__':
    app.start()

