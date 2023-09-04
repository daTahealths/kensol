from django.db import models

class GenBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50) 
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'gen_bellmouth'
        unique_together = (('size', 'motortype'),)

class HighBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50) 
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'high_bellmouth'
        unique_together = (('size', 'motortype'),)