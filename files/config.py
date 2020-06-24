from celery.schedules import crontab

FILES_CELERY_BEAT_SCHEDULE = {
    "remove-files": {
        "task": "remove_expired_files",
        "schedule": crontab(minute="*"),
    },
}