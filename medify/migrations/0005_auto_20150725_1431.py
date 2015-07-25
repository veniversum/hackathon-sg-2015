# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medify', '0004_pharmacy'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('device_name', models.CharField(max_length=200, blank=True)),
                ('description', models.TextField(blank=True)),
                ('gmdn', models.TextField(blank=True)),
                ('speciality', models.TextField(blank=True)),
                ('hs_code', models.CharField(max_length=50, blank=True)),
                ('hsa_product_code', models.CharField(max_length=50, blank=True)),
                ('medical_device_class', models.CharField(max_length=50, blank=True)),
                ('registration_number', models.CharField(max_length=50, blank=True)),
                ('registration_date', models.DateField()),
                ('change_date', models.CharField(max_length=50, blank=True)),
                ('expiry_date', models.DateField()),
                ('product_owner_name', models.TextField(blank=True)),
                ('product_owner_short_name', models.CharField(max_length=200, blank=True)),
                ('product_owner_address', models.TextField(blank=True)),
                ('registrant_name', models.CharField(max_length=200, blank=True)),
                ('registrant_address', models.TextField(blank=True)),
                ('imported_by_name', models.CharField(max_length=200, blank=True)),
                ('imported_by_address', models.TextField(blank=True)),
                ('models_name', models.TextField(blank=True)),
                ('identifier', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='zipcode',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
