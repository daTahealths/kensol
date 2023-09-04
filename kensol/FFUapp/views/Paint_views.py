from django.shortcuts import render
from FFUapp.models.Paint_models import GenPaint, HighPaint

def calculate_paint_price(size, spec):
    if spec == "일반사양":
        model = GenPaint
    elif spec == "고사양":
        model = HighPaint
    else:
        return 0

    paints = model.objects.filter(size=size)

    total_paint_cost = 0  
    for paint in paints:
        square_meter = ((paint.figure_width * paint.figure_length)/1000000) * 2 * paint.necessary_quantity
        paint_cost = square_meter * paint.won_per_meter    

        total_paint_cost += paint_cost  

    return total_paint_cost
