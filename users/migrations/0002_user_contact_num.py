# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact_num',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
    ]