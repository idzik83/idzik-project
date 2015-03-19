# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_usermodel_usermodel_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='usermodel_email',
            field=models.EmailField(unique=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='usermodel_login',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='usermodel_mobile',
            field=models.CharField(unique=True, max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{3}-[0-9]{7}$', message=b'\xd0\x9d\xd0\xb5\xd0\xb2\xd0\xb5\xd1\x80\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x82 \xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80\xd0\xb0')]),
            preserve_default=True,
        ),
    ]
