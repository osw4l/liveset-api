from django.contrib.auth.models import User
from django.db import models
from . import constants


# Create your models here.


class ResourceModel(models.Model):
    name = models.CharField(max_length=20, unique=True)
    order = models.PositiveIntegerField(default=0)
    file = models.FileField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Song(ResourceModel):
    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'


class Video(ResourceModel):
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

