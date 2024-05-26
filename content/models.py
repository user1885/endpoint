from django.db import models
from django.conf import settings

# Create your models here.

class Content(models.Model):
    text = models.TextField()


class Media(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='owned_files')
    content = models.ForeignKey(Content,
                                on_delete=models.CASCADE,
                                related_name='media')
    file = models.FileField(upload_to='content_media/')