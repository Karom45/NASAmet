# Generated by Django 3.0.5 on 2021-03-01 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('classes_id', models.AutoField(db_column='id', default=0, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('class_name', models.CharField(db_column='class_name', max_length=100, verbose_name='Название')),
                ('information', models.TextField(db_column='information', verbose_name='Дополнительная информация')),
            ],
            options={
                'verbose_name': 'Класс метеорита',
                'verbose_name_plural': 'Классы метеоритов',
                'db_table': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Meteorite',
            fields=[
                ('meteorite_id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(db_column='name', max_length=100, verbose_name='Название метеорита')),
                ('mass', models.FloatField(db_column='mass (g)', verbose_name='Масса')),
                ('fall', models.CharField(db_column='fall', max_length=10, verbose_name='Статус')),
                ('year', models.IntegerField(db_column='year', verbose_name='Дата')),
                ('reclat', models.FloatField(db_column='reclat', verbose_name='Широта')),
                ('reclong', models.FloatField(db_column='reclong', verbose_name='Долгота')),
                ('recclass_id', models.ForeignKey(db_column='recclass_id', on_delete=django.db.models.deletion.CASCADE, to='meteorites.Classes')),
            ],
            options={
                'verbose_name': 'Метеорит',
                'verbose_name_plural': 'Метеориты',
                'db_table': 'Meteorites',
            },
        ),
    ]
