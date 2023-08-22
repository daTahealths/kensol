from django.shortcuts import render
from FFUapp.models.Controller_models import GenController, HighController

def calculate_controller_price(size, spec, motortype, motor_company, watt):
    try:    
        if spec == "일반사양":
            model = GenController
        elif spec == "고사양":
            model = HighController
        else:
            return 0

        controller = model.objects.filter(
            size=size,
            motortype=motortype, 
            motor_company=motor_company, 
            watt=watt
        ).first() 

        if controller:
            return controller.controller_price 
        else:
            return 0 

    except Exception as e:
        print(f"Error occurred: {e}")  
        return 0

        