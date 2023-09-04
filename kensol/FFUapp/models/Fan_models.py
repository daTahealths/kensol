from django.db import models

class GenFan(models.Model):
    size = models.CharField(primary_key=True, max_length=50) 
    motortype = models.CharField(max_length=50)
    fan_size = models.CharField(max_length=16)
    fan_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'gen_fan'
        unique_together = (('size', 'motortype'),)

class HighFan(models.Model):
    size = models.CharField(primary_key=True, max_length=50) 
    motortype = models.CharField(max_length=50)
    fan_size = models.CharField(max_length=16)
    fan_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'high_fan'
        unique_together = (('size', 'motortype'),)