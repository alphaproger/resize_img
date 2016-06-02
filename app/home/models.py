from __future__ import unicode_literals
from django.db import models

import os

from app.settings import BASE_DIR

# Create your models here.
class UploadImage(models.Model):
    image = models.ImageField(verbose_name='Select a file', help_text='max. 5 megabytes')
    width = models.IntegerField(null=True, blank=False, default=255, help_text='required')
    height = models.IntegerField(null=True, blank=True, help_text='optional')

    def delete(self, *args, **kwargs):
        os.remove(BASE_DIR + self.image.url)
        super(UploadImage, self).delete(*args, **kwargs)
