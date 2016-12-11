# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basis', '0003_userprofile_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photostype',
            options={'ordering': ['-quantity']},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-datelastvoice']},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default=11, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default=11, max_length=30),
            preserve_default=False,
        ),
    ]
