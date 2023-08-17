from django.db import models

# 일반사양_NCT_가공비
class GenNct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)        # ffu 규격
    nct_price = models.IntegerField()                                 # NCT 판금 가공비

    class Meta:
        managed = False
        db_table = 'gen_nct'


# 고사양_NCT_가공비
class HighNct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)        # ffu 규격
    nct_price = models.IntegerField()                                 # NCT 판금 가공비 

    class Meta:
        managed = False
        db_table = 'high_nct'