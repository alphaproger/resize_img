from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UploadImage(models.Model):
    image = models.ImageField()
    width = models.IntegerField(null=True, blank=False, default=0)
    height = models.IntegerField(null=True, blank=True, default=0)

