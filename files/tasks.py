from celery import task
from .models import File
from django.utils import timezone


@task(name="remove_expired_files")
def remove_expired_files():
    files = File.objects.filter(expires__lte=timezone.now())
    for file in files:
        file.file.delete()
        file.delete()
