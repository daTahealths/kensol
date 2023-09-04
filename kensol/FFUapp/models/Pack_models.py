from django.db import models

class GenPack(models.Model):
    pack_price = models.IntegerField()                              
    size = models.CharField(primary_key=True, max_length=16)        

    class Meta:
        managed = True
        db_table = 'gen_pack'
        unique_together = (('size', 'pack_price'),)

class HighPack(models.Model):
    pack_price = models.IntegerField()                             
    size = models.CharField(primary_key=True, max_length=16)        
    
    class Meta:
        managed = True
        db_table = 'high_pack'
        unique_together = (('size', 'pack_price'),)