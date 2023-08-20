from django.shortcuts import render, redirect
from .Assembly_views import calculate_assembly_price
from .Pack_views import calculate_pack_price
from .NCT_views import calculate_nct_price
from .Volt_views import calculate_volt_price
from .MaterialCost_views import calculate_materialcost_price
from .Paint_views import calculate_paint_price

# 1. 흰색글자로 바꾸기 2. kwargs 대체 방법이나 문제해결 3. 조립인건비 pass문제 해결
포장팔렛트 = "포장팔렛트"
NCT_판금_가공비 = "NCT 판금 가공비"

def get_price_for_item(item_name, size, spec, **kwargs):
    if item_name == "조립인건비":
        # 예: item = Assembly.objects.get(name=size)
        # return item.assembly_price
        pass  # 여기에 실제 구현을 추가하세요.
        
    elif item_name == 포장팔렛트:
        return calculate_pack_price(size, spec)

    elif item_name == NCT_판금_가공비:
        return calculate_nct_price(size, spec)

    elif item_name == "볼트":
        return calculate_volt_price(size, spec)

    elif item_name == "자재비 (AL, SPCC 외)":
        return calculate_materialcost_price(size, spec)

    elif item_name == "도장비":
        return calculate_paint_price(size, spec)
        
    elif item_name == "MOTOR & 컨트롤러":
        motor_type = kwargs.get('motor_type', None)
        return motor_type
        
    elif item_name == "FAN":
        fan_speed = kwargs.get('fan_speed', None)
        return fan_speed
        
    elif item_name == "BELLMOUTH (보호망포함)":
        material = kwargs.get('material', None)
        return material

    else:
        return 0

def ffuInput(request):
    if request.method == 'POST':
        size = request.POST.get('size')
        spec = request.POST.get('spec')
        
        quantity_str = request.POST.get('quantity', '1')
        try:
            quantity = int(quantity_str)
        except ValueError:
            quantity = 1

        names = ['자재비 (AL, SPCC 외)', '도장비', NCT_판금_가공비, 'MOTOR & 컨트롤러', 'FAN', 'BELLMOUTH (보호망포함)', '볼트', '포장용 잡자재', '조립인건비', 포장팔렛트, '운반비']

        items = []
        for name in names:
            # if name == '조립인건비':
            #     unit_price = calculate_assembly_price(size, spec)
            # elif name == '포장팔렛트':
            #     unit_price = calculate_pack_price(size, spec)
            # elif name == 'NCT 판금 가공비':
            #     unit_price = calculate_nct_price(size, spec)
            # else:
            #     unit_price = get_price_for_item(name, size, spec) or 0
            
            try:
                unit_price = get_price_for_item(name, size, spec)

                total_price = unit_price * quantity
                items.append((name, quantity, unit_price, total_price))
            except Exception as e:
                print(f"Error occurred at {name}: {e}")  # 로깅을 위한 출력

        subtotal_unit = sum([item[2] for item in items])
        subtotal_totals = sum([item[3] for item in items])

        context = {
            'items': items,
            'subtotal_unit': subtotal_unit,
            'subtotal_totals': subtotal_totals
        }
        return render(request, 'FFUOutput.html', context)

    return render(request, 'FFUInput.html')


def ffuOutput(request):
    return render(request, 'FFUOutput.html')
