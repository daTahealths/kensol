from django.db import models

class GenAssembly(models.Model):
    assembly_price = models.IntegerField()                          
    size = models.CharField(primary_key=True, max_length=16)       

    class Meta:
        managed = True
        db_table = 'gen_assembly'
        unique_together = (('size', 'assembly_price'),)

class HighAssembly(models.Model):
    assembly_price = models.IntegerField()                         
    size = models.CharField(primary_key=True, max_length=16)      
    
    class Meta:
        managed = True
        db_table = 'high_assembly'
        unique_together = (('size', 'assembly_price'),)
