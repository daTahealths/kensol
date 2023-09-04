from django.db import models

class GenNct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)        
    nct_price = models.IntegerField()                                 

    class Meta:
        managed = True
        db_table = 'gen_nct'


class HighNct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)       
    nct_price = models.IntegerField()                                 

    class Meta:
        managed = True
        db_table = 'high_nct'