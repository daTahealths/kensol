from django.db import models

# 일반사양_도장비
class GenPaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32)    # item
    size = models.CharField(max_length=16)                      # ffu 규격
    figure_width = models.FloatField()                          # 전개 가로
    figure_length = models.FloatField()                         # 전개 세로
    won_per_meter = models.IntegerField()                       # 원/m^2
    necessary_quantity = models.IntegerField()                  # 자재 필요수량

    class Meta:
        managed = False
        db_table = 'gen_paint'
        unique_together = (('item', 'size'),)

# 고사양_도장비
class HighPaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32)    # item
    size = models.CharField(max_length=16)                      # ffu 규격
    figure_width = models.FloatField()                          # 전개 가로
    figure_length = models.FloatField()                         # 전개 세로
    won_per_meter = models.IntegerField()                       # 원/m^2
    necessary_quantity = models.IntegerField()                  # 자재 필요수량
    
    class Meta:
        managed = False
        db_table = 'high_paint'
        unique_together = (('item', 'size'),)