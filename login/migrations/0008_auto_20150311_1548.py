# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150311_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='avatar',
            field=models.ImageField(default=b'C:\\Users\\idzik\\django_project\\Scripts\\idzik_test_project\\media\\no_avatar.png', upload_to=b'%s/%Y/%m'),
            preserve_default=True,
        ),
    ]
