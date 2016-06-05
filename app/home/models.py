from __future__ import unicode_literals
from django.db import models

import os
from conf.settings import BASE_DIR


# Create your models here.
class UploadImage(models.Model):
    class Meta:
        db_table = 'Image'
    image = models.ImageField(verbose_name='Select a file', help_text='max. 5 megabytes')
    width = models.IntegerField(null=True, blank=False)
    height = models.IntegerField(null=True, blank=True)

    def delete(self, *args, **kwargs):
        os.remove(BASE_DIR + self.image.url)
        super(UploadImage, self).delete(*args, **kwargs)
