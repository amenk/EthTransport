# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 22:52
from __future__ import unicode_literals

import audit_log.models.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(editable=False, max_length=40, null=True)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(editable=False, max_length=40, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('flag_approved', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, default=8, max_length=100, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('gallery_type', models.CharField(max_length=5)),
                ('image_data', models.ImageField(blank=True, null=True, upload_to=b'gallery')),
                ('caption', models.CharField(default=b'', max_length=60)),
                ('video_url', models.CharField(blank=True, default=b'', max_length=100, validators=[django.core.validators.URLValidator()])),
                ('created_by', audit_log.models.fields.CreatingUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_guzo_media_set', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', audit_log.models.fields.LastUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_guzo_media_set', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OverviewMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(editable=False, max_length=40, null=True)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(editable=False, max_length=40, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('flag_approved', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, default=8, max_length=100, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('native_name', models.CharField(max_length=100)),
                ('locale', models.CharField(max_length=100)),
                ('number_of_lines', models.PositiveSmallIntegerField()),
                ('number_of_stations', models.PositiveSmallIntegerField()),
                ('transit_type', models.CharField(max_length=100)),
                ('budget', models.IntegerField(default=0)),
                ('daily_ridership', models.IntegerField(default=0)),
                ('operation_start_date', models.DateField()),
                ('operators', models.CharField(max_length=100)),
                ('number_of_vehicles', models.PositiveSmallIntegerField()),
                ('created_by', audit_log.models.fields.CreatingUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_guzo_overviewmetadata_set', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', audit_log.models.fields.LastUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_guzo_overviewmetadata_set', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(editable=False, max_length=40, null=True)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(editable=False, max_length=40, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('flag_approved', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, default=8, max_length=100, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('is_operational', models.BooleanField(default=False)),
                ('long', models.PositiveSmallIntegerField()),
                ('lat', models.PositiveSmallIntegerField()),
                ('created_by', audit_log.models.fields.CreatingUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_guzo_station_set', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', audit_log.models.fields.LastUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_guzo_station_set', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Technical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(editable=False, max_length=40, null=True)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(editable=False, max_length=40, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('flag_approved', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, default=8, max_length=100, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('system_length', models.IntegerField()),
                ('track_gauge', models.CharField(max_length=100)),
                ('top_speed', models.IntegerField()),
                ('electrification', models.CharField(max_length=100)),
                ('created_by', audit_log.models.fields.CreatingUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_guzo_technical_set', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', audit_log.models.fields.LastUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_guzo_technical_set', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='media',
            name='overview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guzo.OverviewMetadata'),
        ),
    ]
