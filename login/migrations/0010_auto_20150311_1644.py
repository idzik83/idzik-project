# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20150311_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='avatar',
            field=models.ImageField(default=b'no_avatar.png', null=True, upload_to=b'%s/%Y/%m', blank=True),
            preserve_default=True,
        ),
    ]
