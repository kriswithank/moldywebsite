# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('markdownmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.MarkdownModel')),
                ('title', models.CharField(max_length=250)),
                ('position', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['position', 'title'],
            },
            bases=('common.markdownmodel',),
        ),
    ]
