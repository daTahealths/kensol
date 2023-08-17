from django.shortcuts import render
from FFUapp.models.MaterialCost_models import GenMaterialcost, HighMaterialcost

def calculate_materialcost_price(size, spec):

    # spec 값에 따라 적절한 모델에서 데이터를 검색
    if spec == "일반사양":
        model = GenMaterialcost
    elif spec == "고사양":
        model = HighMaterialcost
    else:
        return 0  # 오류의 경우 0을 반환

    # 해당 모델에서 size로 데이터 검색
    materialcosts = model.objects.filter(size=size)
    
    if not materialcosts.exists():
        return 0

    # 전체 볼트의 총합을 계산
    calculate_materialcost_price = 0
    for materialcost in materialcosts:
        if materialcost.manufacture_quantity == 0:
            materialcost_weight = 0
        else:
            materialcost_weight = (materialcost.matherialsize_width * materialcost.matherialsize_length * materialcost.rawmaterial_thickness * materialcost.rawmaterial_density / (1000000 * materialcost.manufacture_quantity)) * materialcost.necessary_quantity
    
        rawmaterial_cost = materialcost_weight * materialcost.won_per_kg
        calculate_materialcost_price += rawmaterial_cost

    return calculate_materialcost_price


