# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-27 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160827_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='model_pic',
            field=models.ImageField(default='uploads/031_31.JPG', upload_to=''),
        ),
    ]
