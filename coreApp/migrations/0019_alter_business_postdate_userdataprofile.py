# Generated by Django 4.1.7 on 2023-03-23 07:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coreApp', '0018_business_cover_category_fontawesomeclass_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='postDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 13, 53, 44, 103579), verbose_name='Дата публикации'),
        ),
        migrations.CreateModel(
            name='UserDataProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user/avatar/', verbose_name='Аватар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Данные пользователя',
                'verbose_name_plural': 'Данные пользователя',
            },
        ),
    ]
