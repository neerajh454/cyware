# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True,
                                              max_length=250, verbose_name='Username')),
                ('email', models.EmailField(max_length=250, null=True,
                                            verbose_name='email address', blank=True)),
                ('avatar_url', models.CharField(max_length=250,
                                                null=True, verbose_name='Avatar Url', blank=True)),
                ('gravatar_id', models.CharField(max_length=250,
                                                 null=True, verbose_name='Gravatar Url', blank=True)),
                ('url', models.CharField(max_length=250,
                                         null=True, verbose_name='Url', blank=True)),
                ('html_url', models.CharField(max_length=250,
                                              null=True, verbose_name='Html Url', blank=True)),
                ('followers_url', models.CharField(max_length=250,
                                                   null=True, verbose_name='Followers Url', blank=True)),
                ('following_url', models.CharField(max_length=250,
                                                   null=True, verbose_name='Following Url', blank=True)),
                ('gists_url', models.CharField(max_length=250,
                                               null=True, verbose_name='Gists Url', blank=True)),
                ('starred_url', models.CharField(max_length=250,
                                                 null=True, verbose_name='Starred Url', blank=True)),
                ('subscriptions_url', models.CharField(max_length=250,
                                                       null=True, verbose_name='Subscriptions Url', blank=True)),
                ('organizations_url', models.CharField(max_length=250,
                                                       null=True, verbose_name='Organizations Url', blank=True)),
                ('repos_url', models.CharField(max_length=250,
                                               null=True, verbose_name='Repos Url', blank=True)),
                ('events_url', models.CharField(max_length=250,
                                                null=True, verbose_name='Events Url', blank=True)),
                ('received_events_url', models.CharField(max_length=250,
                                                         null=True, verbose_name='Received Events Url', blank=True)),
                ('user_type', models.CharField(max_length=250,
                                               null=True, verbose_name='User type', blank=True)),
                ('site_admin', models.CharField(max_length=250,
                                                null=True, verbose_name='Site Admin', blank=True)),
                ('score', models.CharField(max_length=250,
                                           null=True, verbose_name='Score', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
