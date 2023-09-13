from django.db import models

class Ffilter(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    filterstyle = models.CharField(max_length=16)
    filterpressure = models.CharField(max_length=16)
    windspeed = models.CharField(max_length=16)
    filter_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ffilter'
        unique_together = (('size', 'filterstyle', 'filterpressure', 'windspeed'),)