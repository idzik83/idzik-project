# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usermodel_surname', models.CharField(max_length=30)),
                ('usermodel_name', models.CharField(max_length=30)),
                ('usermodel_login', models.CharField(max_length=30)),
                ('usermodel_password', models.CharField(max_length=30)),
                ('usermodel_email', models.EmailField(max_length=75)),
                ('usermodel_dob', models.DateField()),
            ],
            options={
                'db_table': 'usermodel',
            },
            bases=(models.Model,),
        ),
    ]
