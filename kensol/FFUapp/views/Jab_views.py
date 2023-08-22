from django.shortcuts import render
from FFUapp.models.Jab_models import GenJab, HighJab

def calculate_jab_price(size, spec):
    """
    주어진 size와 spec에 따라 조립 가격을 반환합니다.
    """ 
    # spec 값에 따라 적절한 모델에서 데이터를 검색
    if spec == "일반사양":
        model = GenJab
    elif spec == "고사양":
        model = HighJab
    else:
        return 0  # 0 또는 적절한 오류 메시지를 반환

    # 해당 모델에서 size로 데이터 검색  ## first() 찾아보기!
    jab = model.objects.filter(size=size).first()
    if jab:
        return jab.jab_price
    else:
        return 0  