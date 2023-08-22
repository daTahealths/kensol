from django.db import models

class GenController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motor_company) found, that is not supported. The first column is selected.
    motor_company = models.CharField(max_length=32)
    watt = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_controller'
        unique_together = (('size', 'motor_company'),)

class HighController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motor_company) found, that is not supported. The first column is selected.
    motor_company = models.CharField(max_length=32)
    watt = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_controller'
        unique_together = (('size', 'motor_company'),)