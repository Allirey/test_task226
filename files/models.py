from django.db import models
from django.urls import reverse


class File(models.Model):
    file = models.FileField(upload_to='uploaded_files/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    expires = models.DateTimeField()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
