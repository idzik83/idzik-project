# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_usermodel_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='avatar',
            field=models.ImageField(default=b'C:\\Users\\idzik\\django_project\\Scripts\\idzik_test_project\\static\\img\\no_avatar.png', upload_to=b'%s/%Y/%m'),
            preserve_default=True,
        ),
    ]
