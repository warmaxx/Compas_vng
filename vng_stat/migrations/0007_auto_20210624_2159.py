# Generated by Django 3.2 on 2021-06-24 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20210624_2159'),
        ('vng_stat', '0006_auto_20210509_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vng_stat.form', verbose_name='Форма проверки'),
        ),
        migrations.AlterField(
            model_name='check',
            name='tek_Object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vng_stat.tek_object', verbose_name='Объект ТЭК'),
        ),
        migrations.AlterField(
            model_name='tek_object',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vng_stat.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='tek_object',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homepage.region', verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='tek_object',
            name='ul',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vng_stat.ul', verbose_name='Юридическое лицо'),
        ),
    ]
