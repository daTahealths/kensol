from django.db import models

class GenAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    assembly_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_assembly'
        unique_together = (('size', 'assembly_price'),)

class HighAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    assembly_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_assembly'
        unique_together = (('size', 'assembly_price'),)
