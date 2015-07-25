# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medify', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approvedmedication',
            old_name='license_holder',
            new_name='licence_holder',
        ),
        migrations.RenameField(
            model_name='approvedmedication',
            old_name='license_no',
            new_name='licence_no',
        ),
    ]
