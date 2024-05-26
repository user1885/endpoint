from django.db import models

# Create your models here.

from django.core.validators import MinValueValidator

# Create your models here.

class Reaction(models.Model):
    likes = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    dislikes = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    class Meta:
        abstract = True