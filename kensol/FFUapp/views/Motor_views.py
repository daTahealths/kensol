from django.shortcuts import render
from FFUapp.models.Motor_models import GenMotor, HighMotor

def calculate_motor_price(size, spec, motortype, motor_company, watt):
    try:    
        if spec == "일반사양":
            model = GenMotor
        elif spec == "고사양":
            model = HighMotor
        else:
            return 0

        motor = model.objects.filter(
            size=size,
            motortype=motortype, 
            motor_company=motor_company, 
            watt=watt
        ).first() 

        if motor:
            return motor.motor_price 
        else:
            return 0 

    except Exception as e:
        print(f"Error occurred: {e}")  
        return 0

        