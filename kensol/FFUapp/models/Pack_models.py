from django.db import models

# 일반사양_포장
class GenPack(models.Model):
    # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField()                              # 가격
    size = models.CharField(primary_key=True, max_length=16)        # 규격

    class Meta:
        managed = False
        db_table = 'gen_pack'
        unique_together = (('size', 'pack_price'),)

# 고사양_포장
class HighPack(models.Model):
    # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField()                              # 가격
    size = models.CharField(primary_key=True, max_length=16)        # 규격 
    
    class Meta:
        managed = False
        db_table = 'high_pack'
        unique_together = (('size', 'pack_price'),)