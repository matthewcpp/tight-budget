# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget_api', '0002_auto_20150728_0646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorytemplate',
            old_name='template',
            new_name='budget_template',
        ),
        migrations.AddField(
            model_name='budgettemplate',
            name='total_amount',
            field=models.FloatField(default=0.0),
        ),
    ]
