from django.db import models

class GenVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  
    volt_name = models.CharField(max_length=50)                 
    volt_price = models.IntegerField()                          
    volt_count = models.IntegerField()                          

    class Meta:
        managed = True
        db_table = 'gen_volt'
        unique_together = (('size', 'volt_name'),)

class HighVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50) 
    volt_name = models.CharField(max_length=50)
    volt_price = models.IntegerField()
    volt_count = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'high_volt'
        unique_together = (('size', 'volt_name'),)