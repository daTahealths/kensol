from django.db import models

# 일반사양_자재비
class GenMaterialcost(models.Model):
    # The composite primary key (item, size) found, that is not supported. The first column is selected.
    item = models.CharField(primary_key=True, max_length=32)    # item
    size = models.CharField(max_length=16)                      # ffu 규격
    matherialsize_width = models.FloatField()                   # 자재사이즈 가로
    matherialsize_length = models.FloatField()                  # 자재사이스 세로
    rawmaterial_thickness = models.FloatField()                 # 원자재 두께
    rawmaterial_density = models.FloatField()                   # 원자재 비중
    manufacture_quantity = models.IntegerField()                # 자재 가공수량
    necessary_quantity = models.IntegerField()                  # 자재 필요수량
    won_per_kg = models.IntegerField()                          # 원/kg

    class Meta:
        managed = True
        db_table = 'gen_materialcost'
        unique_together = (('item', 'size'),)

# 고사양_자재비
class HighMaterialcost(models.Model):
    item = models.CharField(primary_key=True, max_length=32)    # item
    size = models.CharField(max_length=16)                      # ffu 규격
    matherialsize_width = models.FloatField()                   # 자재사이즈 가로
    matherialsize_length = models.FloatField()                  # 자재사이스 세로
    rawmaterial_thickness = models.FloatField()                 # 원자재 두께
    rawmaterial_density = models.FloatField()                   # 원자재 비중
    manufacture_quantity = models.IntegerField()                # 자재 가공수량
    necessary_quantity = models.IntegerField()                  # 자재 필요수량
    won_per_kg = models.IntegerField()                          # 원/kg

    class Meta:
        managed = True
        db_table = 'high_materialcost'
        unique_together = (('item', 'size'),)

