from multi_write_celery.celery import app

@app.task
def multi_write(path, content):
    with open(path, "w") as wf:
        wf.write(content)

