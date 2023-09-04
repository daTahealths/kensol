from django.shortcuts import render
from FFUapp.models.Fan_models import GenFan, HighFan

def calculate_fan_price(size, spec, motortype):
    try:    
        if spec == "일반사양":
            model = GenFan
        elif spec == "고사양":
            model = HighFan
        else:
            return 0

        fan = model.objects.filter(
            size=size,
            motortype=motortype
        ).first() 

        if fan:
            return fan.fan_price 
        else:
            return 0 

    except Exception as e:
        print(f"Error occurred: {e}")  
        return 0

        