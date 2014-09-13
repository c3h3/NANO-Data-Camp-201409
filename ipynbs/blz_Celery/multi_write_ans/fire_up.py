from multi_write_celery.tasks import multi_write

jobs = []
for ind in range(10):
    job = ("No_{ind}.csv".format(ind=ind), "I'm file No.{ind}!!".format(ind=ind))
    jobs.append(job)

for file, content in jobs:
    multi_write.delay(file, content)
