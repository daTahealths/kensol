from django.db import models

# 일반사양_조립
class GenAssembly(models.Model):
    # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField()                          # 가격
    size = models.CharField(primary_key=True, max_length=16)        # 규격  

    class Meta:
        managed = True
        db_table = 'gen_assembly'
        unique_together = (('size', 'assembly_price'),)

# 고사양_조립
class HighAssembly(models.Model):
    # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField()                          # 가격
    size = models.CharField(primary_key=True, max_length=16)        # 규격  
    
    class Meta:
        managed = True
        db_table = 'high_assembly'
        unique_together = (('size', 'assembly_price'),)
