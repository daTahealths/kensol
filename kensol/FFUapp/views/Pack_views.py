from django.shortcuts import render
from FFUapp.models.Pack_models import GenPack, HighPack

def calculate_pack_price(size, spec):
    """
    주어진 size와 spec에 따라 조립 가격을 반환합니다.
    """ 
    # spec 값에 따라 적절한 모델에서 데이터를 검색
    if spec == "일반사양":
        model = GenPack
    elif spec == "고사양":
        model = HighPack
    else:
        return 0  # 0 또는 적절한 오류 메시지를 반환

    # 해당 모델에서 size로 데이터 검색
    pack = model.objects.filter(size=size).first()
    if pack:
        return pack.pack_price 
    else:
        return 0  
