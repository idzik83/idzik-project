# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20150309_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='avatar',
            field=models.ImageField(default=b'C:\\Users\\idzik\\django_project\\Scripts\\idzik_test_project\\media\\no_avatar.png', height_field=207, width_field=150, upload_to=b'%s/%Y/%m'),
            preserve_default=True,
        ),
    ]
