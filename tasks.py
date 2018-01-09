from celery import Celery


celery = Celery('NOTIFIER_TASKS', include='sms_tasks')

# Loads settings for Backend to store results of jobs
celery.config_from_object('celeryconfig')

if __name__ == '__main__':
    celery.start()
