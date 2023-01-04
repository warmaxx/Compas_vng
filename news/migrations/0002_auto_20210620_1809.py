# Generated by Django 3.2 on 2021-06-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date_create',
            field=models.DateField(auto_now=True, verbose_name='Дата создания / редактирования новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date_end',
            field=models.DateField(verbose_name='Дата до которой нужно показывать новость'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date_start',
            field=models.DateField(verbose_name='Дата с которой нужно показывать новость'),
        ),
    ]