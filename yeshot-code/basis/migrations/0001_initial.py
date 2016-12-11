# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 07:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('datelastcomment', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datelike', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photofile', models.ImageField(upload_to='photofile')),
                ('likeds', models.IntegerField(default=0)),
                ('dateupload', models.CharField(max_length=120)),
                ('photosay', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Photostype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=120)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('commentsquantity', models.IntegerField(default=0)),
                ('discribtion', models.CharField(max_length=120)),
                ('datelastvoice', models.CharField(max_length=120)),
                ('postuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.ImageField(blank=True, default='profile_head/default_head.jpg', upload_to='profile_head')),
                ('mylikesquantity', models.IntegerField(default=0)),
                ('groups_id', models.IntegerField(default=0)),
                ('photosquantity', models.IntegerField(default=0)),
                ('profileuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='photos',
            name='phototype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basis.Photostype'),
        ),
        migrations.AddField(
            model_name='photos',
            name='photouser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='likes',
            name='likedphoto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basis.Photos'),
        ),
        migrations.AddField(
            model_name='likes',
            name='likeduser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='commenttopost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basis.Posts'),
        ),
        migrations.AddField(
            model_name='comments',
            name='commentuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
