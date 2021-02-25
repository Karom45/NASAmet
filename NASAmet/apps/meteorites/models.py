from django.db import models

# Create your models here.


class Classes(models.Model):

    class Meta:
        db_table = 'Classes'

    classes_id = models.IntegerField(primary_key=True, db_column='id')
    class_name = models.CharField(max_length=100, db_column='class_name')
    information = models.TextField(db_column='information')


class Meteorite(models.Model):

    class Meta:
        db_table = 'Meteorites'

    meteorite_id = models.IntegerField(primary_key=True, db_column='id')
    name = models.CharField(max_length=100, db_column='name')
    recclass_id = models.ForeignKey('Classes' , db_column='recclass_id' , on_delete = models.CASCADE)
    mass = models.FloatField(db_column='mass (g)')
    fall = models.CharField(max_length=10, db_column='mass (g)')
    year = models.DateField(db_column='year')
    reclat = models.FloatField(db_column='reclat')
    reclong = models.FloatField(db_column='reclong')
    geoLocation = models.CharField(db_column='GeoLocation')