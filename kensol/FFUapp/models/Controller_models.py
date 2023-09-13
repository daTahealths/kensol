from django.db import models

class GenController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_controller'
        unique_together = (('size', 'motortype', 'ph'),)

class HighController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motortype, ph) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_controller'
        unique_together = (('size', 'motortype', 'ph'),)