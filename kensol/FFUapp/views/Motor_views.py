from django.shortcuts import render
from FFUapp.models.Motor_models import GenMotor, HighMotor

# 삼성전자의 지역들을 삼성전자로 통합 (motor & controller에 적용)
def convert_location(location):
    samsung_locations = ["삼성전자 천안", "삼성전자 평택", "삼성전자 화성", "삼성전자 기흥"]
    if location in samsung_locations:
        return "삼성전자"
    else:
        return location or ''

def calculate_motor_price(size, spec, motortype, ph, location=None):
    location = convert_location(location)
    try:    
        if spec == "일반사양":
            model = GenMotor
        elif spec == "고사양":
            model = HighMotor
        else:
            return 0

        if location:
            motor = model.objects.filter(
                size=size,
                motortype=motortype, 
                ph=ph,
                location=location
            ).first()
        else:
            motor = model.objects.filter(
                size=size,
                motortype=motortype, 
                ph=ph,
                location=''
            ).first()

        if motor:
            return motor.motor_price 
        else:
            return 0 

    except Exception as e:
        print(f"Error occurred: {e}")  
        return 0

        