from django.db import models

# 일반사양볼트
class GenVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50)                 # 볼트_품명+규격
    volt_price = models.IntegerField()                          # 볼트_단가
    volt_count = models.IntegerField()                          # 볼트_수량

    class Meta:
        managed = False
        db_table = 'gen_volt'
        unique_together = (('size', 'volt_name'),)

# 고사양볼트
class HighVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50)
    volt_price = models.IntegerField()
    volt_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_volt'
        unique_together = (('size', 'volt_name'),)