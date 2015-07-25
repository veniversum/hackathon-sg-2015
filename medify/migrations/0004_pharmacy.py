# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medify', '0003_auto_20150725_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pharmacy_name', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=50)),
                ('coords', models.CharField(max_length=50)),
            ],
        ),
    ]
