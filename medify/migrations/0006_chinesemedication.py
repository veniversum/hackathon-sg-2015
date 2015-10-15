# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medify', '0005_auto_20150725_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChineseMedication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=100)),
                ('brand_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('dosage_form', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
    ]
