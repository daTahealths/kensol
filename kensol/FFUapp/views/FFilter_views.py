from django.shortcuts import render
from FFUapp.models.FFilter_models import Ffilter

def calculate_ffilter_price(size, filterstyle, filterpressure):
    ffilter = Ffilter.objects.filter(
        size=size,
        filterstyle=filterstyle, 
        filterpressure=filterpressure
    ).first() 

    if ffilter:
        return ffilter.filter_price 
    else:
        return 0


        