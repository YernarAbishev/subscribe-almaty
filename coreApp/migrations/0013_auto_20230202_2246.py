# Generated by Django 3.1 on 2023-02-02 16:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0012_auto_20230202_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='querytest',
            name='master',
        ),
        migrations.RemoveField(
            model_name='querytest',
            name='service',
        ),
        migrations.AlterField(
            model_name='business',
            name='postDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 2, 22, 46, 33, 127221), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='querytest',
            name='business',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='coreApp.business', verbose_name='Компания'),
        ),
    ]
