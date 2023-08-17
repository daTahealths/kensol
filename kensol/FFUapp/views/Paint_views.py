from django.shortcuts import render
from FFUapp.models.Paint_models import GenPaint, HighPaint

def calculate_paint_price(size, spec):

    # spec 값에 따라 적절한 모델에서 데이터를 검색
    if spec == "일반사양":
        model = GenPaint
    elif spec == "고사양":
        model = HighPaint
    else:
        return 0  # 오류의 경우 0을 반환

    # 해당 모델에서 size로 데이터 검색
    paints = model.objects.filter(size=size)

    total_paint_cost = 0  # <-- 변수 이름을 변경했습니다.
    for paint in paints:
        square_meter = ((paint.figure_width * paint.figure_length)/1000000)*2
        paint_cost = square_meter * paint.won_per_meter    

        total_paint_cost += paint_cost  # <-- 변수 이름을 변경했습니다.

    return total_paint_cost  # <-- 변수 이름을 변경했습니다.
