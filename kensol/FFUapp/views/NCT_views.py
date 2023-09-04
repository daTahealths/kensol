from django.shortcuts import render
from FFUapp.models.NCT_models import GenNct, HighNct

def calculate_nct_price(size, spec):
    if spec == "일반사양":
        model = GenNct
    elif spec == "고사양":
        model = HighNct
    else:
        return 0  

    nct = model.objects.filter(size=size).first()
    if nct:
        return nct.nct_price
    else:
        return 0  
