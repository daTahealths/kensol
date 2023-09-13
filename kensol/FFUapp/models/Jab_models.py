from django.db import models

class GenJab(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    jab_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'gen_jab'

class HighJab(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    jab_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_jab'