# Generated by Django 3.2 on 2021-05-01 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vng_stat', '0004_alter_check_date_latest_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tek_object',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='Название объекта'),
        ),
        migrations.AlterField(
            model_name='tek_object',
            name='place',
            field=models.CharField(max_length=1000, verbose_name='Местонахождение объекта'),
        ),
        migrations.AlterField(
            model_name='ul',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='Название юридического лица'),
        ),
        migrations.AlterField(
            model_name='ul',
            name='place',
            field=models.CharField(max_length=1000, verbose_name='Местонахождение юридического лица'),
        ),
    ]