# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medify', '0002_auto_20150725_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='illegalmedication',
            name='dosage_form_colour',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='illegalmedication',
            name='adulterant_type',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='illegalmedication',
            name='country',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='illegalmedication',
            name='dosage_form',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='illegalmedication',
            name='dosage_form_marking',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='illegalmedication',
            name='dosage_form_shape',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='illegalmedication',
            name='manufacturer',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='illegalmedication',
            name='remarks',
            field=models.TextField(blank=True),
        ),
    ]
