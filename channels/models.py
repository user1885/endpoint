from django.db import models
from django.utils import timezone
from django.conf import settings
from reaction.models import Reaction
from content.models import Content

# Create your models here.

class Channel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='owned_channels')
    subscribers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                         related_name='channels')
    


class Post(Reaction):
    channel = models.ForeignKey(Channel,
                                on_delete=models.CASCADE,
                                related_name='posts')
    publish_date = models.DateTimeField(default=timezone.now)
    content = models.OneToOneField(Content,
                                   on_delete=models.CASCADE,
                                   related_name='post')


class Comment(Reaction):
    post = models.ForeignKey(Post, 
                             on_delete=models.CASCADE, 
                             related_name='comments')
    reply_to = models.ForeignKey('self', 
                                 on_delete=models.CASCADE, 
                                 related_name='replies')
