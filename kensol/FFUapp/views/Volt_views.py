from django.shortcuts import render
from FFUapp.models.Volt_models import GenVolt, HighVolt

def calculate_volt_price(size, spec):
    if spec == "일반사양":
        model = GenVolt
    elif spec == "고사양":
        model = HighVolt
    else:
        return 0

    volts = model.objects.filter(size=size)
    
    volt_subtotal = 0
    for volt in volts:
        volt_amount = volt.volt_price * volt.volt_count
        volt_subtotal += volt_amount

    calculate_volt_price = volt_subtotal * 1.5
    return calculate_volt_price
