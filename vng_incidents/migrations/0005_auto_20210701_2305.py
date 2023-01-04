# Generated by Django 3.2 on 2021-07-01 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vng_incidents', '0004_alter_incident_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='date_time',
            field=models.DateTimeField(verbose_name='Дата и время происшествия'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='result',
            field=models.TextField(blank=True, verbose_name='Результат'),
        ),
    ]
