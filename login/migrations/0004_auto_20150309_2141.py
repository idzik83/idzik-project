# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20150223_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='usermodel_dob',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='usermodel_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='usermodel_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='usermodel_password',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='usermodel_login',
            new_name='login',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='usermodel_mobile',
            new_name='mobile',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='usermodel_surname',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='password',
            field=models.CharField(default=datetime.datetime(2015, 3, 9, 21, 41, 57, 132130, tzinfo=utc), max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
