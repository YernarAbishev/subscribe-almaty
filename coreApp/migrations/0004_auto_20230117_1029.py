# Generated by Django 3.1 on 2023-01-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0003_auto_20230117_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]