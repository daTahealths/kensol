from django.db import models

class LoadQuantity(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, ea) found, that is not supported. The first column is selected.
    ea = models.IntegerField()
    carsize = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'load_quantity'
        unique_together = (('size', 'ea'),)


class LocationMovecost(models.Model):
    location = models.CharField(primary_key=True, max_length=50)  # The composite primary key (location, carsize) found, that is not supported. The first column is selected.
    carsize = models.CharField(max_length=50)
    move_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'location_movecost'
        unique_together = (('location', 'carsize'),)