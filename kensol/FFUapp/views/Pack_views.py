from django.shortcuts import render
from FFUapp.models.Pack_models import GenPack, HighPack

def calculate_pack_price(size, spec):
    if spec == "일반사양":
        model = GenPack
    elif spec == "고사양":
        model = HighPack
    else:
        return 0 

    pack = model.objects.filter(size=size).first()
    if pack:
        return pack.pack_price 
    else:
        return 0  
