from django.db import models

# Create your models here.


class Classes(models.Model):

    class Meta:
        db_table = 'Classes'
        verbose_name = 'Класс метеорита'
        verbose_name_plural = 'Классы метеоритов'

    classes_id = models.IntegerField('id', primary_key=True, db_column='id')
    class_name = models.CharField('Название', max_length=100, db_column='class_name')
    information = models.TextField('Дополнительная информация', db_column='information')

    def __str__(self):
        return self.class_name


class Meteorite(models.Model):

    class Meta:
        db_table = 'Meteorites'
        verbose_name = 'Метеорит'
        verbose_name_plural = 'Метеориты'

    meteorite_id = models.IntegerField('id' ,primary_key=True, db_column='id')
    name = models.CharField('Название метеорита' ,max_length=100, db_column='name')
    # recclass_id = models.IntegerField('Класс', db_column='recclass_id')
    recclass_id = models.ForeignKey('Classes' , db_column='recclass_id', on_delete = models.CASCADE)
    mass = models.FloatField('Масса', db_column='mass (g)')
    fall = models.CharField('Статус' , max_length=10, db_column='fall')
    year = models.DateField('Дата', db_column='year')
    reclat = models.FloatField('Широта',db_column='reclat')
    reclong = models.FloatField('Долгота', db_column='reclong')
    geoLocation = models.CharField('Координаты',max_length=100, db_column='GeoLocation')

    def __str__(self):
        return self.name