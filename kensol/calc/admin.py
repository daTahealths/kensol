from django.contrib import admin
from calc import models

# Register your models here.
admin.site.register(models.Casing)
admin.site.register(models.RawMaterial)
admin.site.register(models.RawMaterialThickness)
admin.site.register(models.PlanarFigureSize)
admin.site.register(models.MaterialSize)
admin.site.register(models.MaterialCost)
admin.site.register(models.Estimate)
admin.site.register(models.PaintCost)
admin.site.register(models.Option)