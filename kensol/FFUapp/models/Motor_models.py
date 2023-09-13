from django.db import models

class GenMotor(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_motor'
        unique_together = (('size', 'motortype', 'ph'),)

class HighMotor(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_motor'
        unique_together = (('size', 'motortype', 'ph'),)