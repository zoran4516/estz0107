# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 08:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20180421_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactadmin',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='contact', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', '.doc', '.docx', '.xlsx', '.xls'])], verbose_name='Файл вложения (не более 20 мб)'),
        ),
        migrations.AlterField(
            model_name='contactadmin',
            name='message',
            field=models.TextField(blank=True, verbose_name='Текст сообщения'),
        ),
        migrations.AlterField(
            model_name='contactadmin',
            name='patronymic',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='contactadmin',
            name='post',
            field=models.CharField(choices=[('R', 'Руководитель компании'), ('P', 'Представитель компании'), ('I', 'Индивидуальный предприниматель'), ('Z', 'Инженер компании'), ('G', 'Государственный служащий'), ('F', 'Гражданин РФ'), ('S', 'Студент'), ('E', 'Пенсионер'), ('O', 'Общественный деятель'), ('C', 'Представитель СРО'), ('D', 'Депутат'), ('C', 'Судья'), ('U', 'Представитель прокуратуры'), ('M', 'Представитель органов МВД / ФСБ'), ('N', 'Представитель налоговой службы')], default='G', max_length=1, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='contactadmin',
            name='work_place',
            field=models.TextField(max_length=2000, verbose_name='Место работы'),
        ),
    ]
