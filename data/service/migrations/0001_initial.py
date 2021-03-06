# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-08 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time', models.DateTimeField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField()),
                ('home_id', models.IntegerField()),
                ('data_type', models.IntegerField(choices=[(0, 'heart rate'), (1, 'nutritional intake'), (2, 'body temperature'), (3, 'medication intake'), (4, 'stress level'), (5, 'exercise activity')])),
                ('int_val1', models.IntegerField(blank=True, null=True)),
                ('int_val2', models.IntegerField(blank=True, null=True)),
                ('flt_val1', models.FloatField(blank=True, null=True)),
                ('flt_val2', models.FloatField(blank=True, null=True)),
                ('str_val', models.CharField(max_length=200)),
                ('device_create_time', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
