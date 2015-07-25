# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedMedication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_no', models.CharField(unique=True, max_length=9)),
                ('product_name', models.CharField(max_length=100)),
                ('license_holder', models.CharField(max_length=100)),
                ('approval_date', models.DateField()),
                ('f_class', models.CharField(max_length=50)),
                ('atc_code', models.CharField(max_length=50, blank=True)),
                ('dosage_form', models.CharField(max_length=50)),
                ('route', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=50)),
                ('active_ingredients', models.TextField()),
                ('strength', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IllegalMedication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=100)),
                ('dosage_form', models.CharField(max_length=50)),
                ('dosage_form_shape', models.CharField(max_length=50)),
                ('dosage_form_marking', models.CharField(max_length=50)),
                ('adulterant_type', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=200)),
                ('remarks', models.TextField()),
            ],
        ),
    ]
