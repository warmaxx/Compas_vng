# Generated by Django 3.2 on 2021-06-30 19:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_delete_departament'),
        ('vng_incidents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incident',
            options={'verbose_name': 'Происшествие', 'verbose_name_plural': 'Происшествия'},
        ),
        migrations.AlterField(
            model_name='incident',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата и время происшествия'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homepage.region', verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='source',
            field=models.CharField(choices=[('СМИ', 'СМИ'), ('Доклад тер. подр.', 'Доклад тер. подр.')], max_length=20, verbose_name='Источник'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='subject',
            field=models.CharField(choices=[('Объект ТЭК', 'Объект ТЭК'), ('Ведомственная охрана', 'Ведомственная охрана')], max_length=22, verbose_name='Субъект происшествия'),
        ),
    ]