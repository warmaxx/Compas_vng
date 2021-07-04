# Generated by Django 3.2 on 2021-06-24 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_remove_departament_region'),
        ('phonebook', '0004_alter_contact_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Полное название звания')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Адрес местонахождения отдела')),
                ('region', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='homepage.region', verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.IntegerField(choices=[(0, 'На службе'), (1, 'Болен'), (2, 'Коммандировка'), (3, 'Отпуск'), (4, 'Декрет'), (5, 'Уволен'), (6, 'Пенсия'), (7, 'Переведен')], max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='departament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='phonebook.departament', verbose_name='Отдел'),
        ),
    ]