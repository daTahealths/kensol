from django.shortcuts import render
from FFUapp.models.Bellmouth_models import GenBellmouth, HighBellmouth

def calculate_bellmouth_price(size, spec, motortype):
    try:    
        if spec == "일반사양":
            model = GenBellmouth
        elif spec == "고사양":
            model = HighBellmouth
        else:
            return 0

        bellmouth = model.objects.filter(
            size=size,
            motortype=motortype
        ).first() 

        if bellmouth:
            return bellmouth.bellmouth_price 
        else:
            return 0 

    except Exception as e:
        print(f"Error occurred: {e}")  
        return 0

        