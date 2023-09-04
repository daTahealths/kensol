from django.shortcuts import render
from FFUapp.models.Jab_models import GenJab, HighJab

def calculate_jab_price(size, spec):
    if spec == "일반사양":
        model = GenJab
    elif spec == "고사양":
        model = HighJab
    else:
        return 0  

    jab = model.objects.filter(size=size).first()
    if jab:
        return jab.jab_price
    else:
        return 0  