# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-27 04:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0005_basicpost_body_html'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('titledbasicpost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.TitledBasicPost')),
                ('position', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['position', 'title'],
            },
            bases=('common.titledbasicpost',),
        ),
    ]
