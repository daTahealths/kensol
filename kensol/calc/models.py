from django.db import models

# 원자재
class RawMaterial(models.Model):
    quality = models.CharField(max_length = 50)     # 재질
    weight = models.FloatField()                    # 비중
 
# 원자재_두께
class RawMaterialThickness(models.Model):
    raw_material = models.ForeignKey(RawMaterial,
                                        on_delete = models.SET_NULL,
                                        null = True)
    thickness = models.FloatField()   # 두께

# 전개 사이즈
class PlanarFigureSize(models.Model):
    width = models.FloatField()                     # 가로
    length = models.FloatField()                    # 세로

    @property
    def 중량(self):
        return (self.width * self.length
                * self.casing.raw_material_thickness.thickness * self.casing.raw_material_thickness.raw_material.weight) / 1000000 * self.casing.necessary_quantity


# 자재 사이즈
class MaterialSize(models.Model):
    width = models.FloatField()                     # 가로
    length = models.FloatField()                    # 세로
    manufacture_quantity = models.IntegerField()                # 가공수량

# 자재비
class MaterialCost(models.Model):
    won_per_kg = models.FloatField()                     # 원/kg
    
    @property
    def 중량(self):                                 # 중량
        return (self.casing.MaterialSize.width * self.casing.MaterialSize.length
                * self.casing.raw_material_thickness.thickness
                * self.casing.raw_material_thickness.raw_material.weight / 1000000) / self.casing.MaterialSize.manufacture_quantity * self.casing.necessary_quantity

    @property
    def 원자재금액(self):                           # 원자재금액
        return self.won_per_kg * self.중량


# 견적
class Estimate(models.Model):
    size = models.CharField(max_length = 50)            # 규격
    motorType = models.CharField(max_length = 50)       # 모터 종류
    spec = models.CharField(max_length = 50)        # 일반 / 고사양

# 도장비
class PaintCost(models.Model):
    won_per_square_meter = models.FloatField()                     # 원/m^2

    @property
    def square_meter(self):                                 # m^2
        return (self.PlanarFigureSize.width * self.PlanarFigureSize.length) / 1000000 * 2

    @property
    def 도장금액(self):                           # 도장금액
        return self.square_meter * self.won_per_square_meter


# Casing
class Casing(models.Model):
    item = models.CharField(max_length = 50)       # 이름
    necessary_quantity = models.IntegerField()                # 필요수량
    estimate = models.ForeignKey(Estimate,          # 견적
                                    related_name = 'casings',
                                    on_delete = models.SET_NULL,
                                    null = True)
    raw_material_thickness = models.OneToOneField(RawMaterialThickness,    # 원자재_두께
                                            on_delete = models.SET_NULL,
                                            
                                            null = True)
    planar_figure_size = models.OneToOneField(PlanarFigureSize,                              # 전개 사이즈
                                related_name = 'casing',
                                on_delete = models.SET_NULL,
                                null = True)
    material_size = models.OneToOneField(MaterialSize,                              # 자재 사이즈
                                related_name = 'casing',
                                on_delete = models.SET_NULL,
                                null = True)
    material_cost = models.OneToOneField(MaterialCost,                              # 자재비
                                related_name = 'casing',
                                on_delete = models.SET_NULL,
                                null = True)
    paint_cost = models.OneToOneField(PaintCost,                              # 도장비
                                related_name = 'casing',
                                on_delete = models.SET_NULL,
                                null = True)

# Option
class Option(models.Model):
    item = models.CharField(max_length = 50)       # 이름
    necessary_quantity = models.IntegerField()                # 필요수량
    estimate = models.ForeignKey(Estimate,          # 견적
                                    related_name = 'option',
                                    on_delete = models.SET_NULL,
                                    null = True)
    raw_material_thickness = models.OneToOneField(RawMaterialThickness,    # 원자재_두께
                                            on_delete = models.SET_NULL,
                                            
                                            null = True)
    planar_figure_size = models.OneToOneField(PlanarFigureSize,                              # 전개 사이즈
                                related_name = 'option',
                                on_delete = models.SET_NULL,
                                null = True)
    material_size = models.OneToOneField(MaterialSize,                              # 자재 사이즈
                                related_name = 'option',
                                on_delete = models.SET_NULL,
                                null = True)
    material_cost = models.OneToOneField(MaterialCost,                              # 자재비
                                related_name = 'option',
                                on_delete = models.SET_NULL,
                                null = True)
    paint_cost = models.OneToOneField(PaintCost,                              # 도장비
                                related_name = 'option',
                                on_delete = models.SET_NULL,
                                null = True)

# -----------------------------------------------------------------------------------------

