# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbtest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='client_organization',
            field=models.TextField(default='', max_length=256, verbose_name=b'Deliverable'),
            preserve_default=False,
        ),
    ]