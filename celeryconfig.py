from celery.schedules import crontab

BROKER_URL = 'mongodb://localhost:27017/jobs'

CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "127.0.0.1",
    "port": 27017,
    "database": "jobs",
    "taskmeta_collection": "stock_taskmeta_collection",
}

CELERYBEAT_SCHEDULE = {
    'every-minute': {
        'task': 'tasks.add',
        'schedule': crontab(minute='*/1', hour='9-15', day_of_week='mon-fri'),
        'args': (1, 2),
    },
    'check-status': {
        'task': 'sms_tasks.send_sms',
        'schedule': crontab(minute='*/5'),
    },
}

CELERY_TIMEZONE = 'Asia/Kolkata'
