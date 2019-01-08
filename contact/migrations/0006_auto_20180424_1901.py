# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 16:01
from __future__ import unicode_literals

import contact.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20180424_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactadmin',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='contact/%Y/', validators=[contact.validators.FileValidator(allowed_extensions=['pdf', 'doc', 'docx', 'xlsx', 'xls'], max_size=20971520)], verbose_name='Файл вложения (не более 20 мб)'),
        ),
        migrations.AlterField(
            model_name='contactadmin',
            name='work_place',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Место работы'),
        ),
    ]
