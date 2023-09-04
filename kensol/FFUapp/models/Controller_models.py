from django.db import models

class GenController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  
    motortype = models.CharField(max_length=16)
    motor_company = models.CharField(max_length=32)
    watt = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'gen_controller'
        unique_together = (('size', 'motor_company'),)

class HighController(models.Model):
    size = models.CharField(primary_key=True, max_length=16) 
    motortype = models.CharField(max_length=16)
    motor_company = models.CharField(max_length=32)
    watt = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'high_controller'
        unique_together = (('size', 'motor_company'),)