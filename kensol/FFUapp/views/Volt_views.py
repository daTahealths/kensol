from django.shortcuts import render
from FFUapp.models.Volt_models import GenVolt, HighVolt

def calculate_volt_price(size, spec):
    """
    주어진 size와 spec에 따라 전체 볼트 가격을 계산하고 반환합니다.
    """ 
    # spec 값에 따라 적절한 모델에서 데이터를 검색
    if spec == "일반사양":
        model = GenVolt
    elif spec == "고사양":
        model = HighVolt
    else:
        return 0  # 오류의 경우 0을 반환

    # 해당 모델에서 size로 데이터 검색
    volts = model.objects.filter(size=size)
    
    # 전체 볼트의 총합을 계산
    volt_subtotal = 0
    for volt in volts:
        volt_amount = volt.volt_price * volt.volt_count
        volt_subtotal += volt_amount

    calculate_volt_price = volt_subtotal * 1.5
    return calculate_volt_price
