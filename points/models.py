from django.db import models
from django.conf import settings

# Create your models here.

class Point(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='point_pictures/')