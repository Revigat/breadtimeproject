# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breadtimesite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(height_field='200', upload_to='static/img/upload', width_field='200'),
        ),
    ]
