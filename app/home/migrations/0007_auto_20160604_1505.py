# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-04 15:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20160602_1111'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='uploadimage',
            table='Image',
        ),
    ]