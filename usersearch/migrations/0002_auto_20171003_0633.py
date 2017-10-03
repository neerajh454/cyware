# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-03 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=250, null=True)),
                ('value', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='userdetails',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'%Y/%m/%d'),
        ),
    ]
