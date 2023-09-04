from django.shortcuts import render, redirect
from .Assembly_views import calculate_assembly_price
from .Pack_views import calculate_pack_price
from .NCT_views import calculate_nct_price
from .Volt_views import calculate_volt_price
from .MaterialCost_views import calculate_materialcost_price
from .Paint_views import calculate_paint_price
from .Jab_views import calculate_jab_price
from .Motor_views import calculate_motor_price
from .Controller_views import calculate_controller_price
from .Fan_views import calculate_fan_price
from .Bellmouth_views import calculate_bellmouth_price
from .excel_views import download_excel, export_to_excel
from .Move_views import calculate_carsize, calculate_moveprice


## 할일 : 단가와 합계를 소수에서 정수로 표현하기
자재비 = "자재비 (AL, SPCC 외)"
도장비 = "도장비"
NCT_가공비 = "NCT 가공비"
MOTOR = "MOTOR"
컨트롤러 = "컨트롤러"
FAN = "FAN"
BELLMOUTH = "BELLMOUTH (보호망포함)"
볼트 = "볼트&리벳"
포장용잡자재 = "포장용 잡자재"
조립인건비 = "조립인건비"
포장팔렛트 = "포장팔렛트"
운반비 = "운반비"
일반사양 = "일반사양"
고사양 = "고사양"

# OUTPUT 항목과 연관된 변수
def get_price_for_item(item_name, size, spec, quantity=None, motortype=None, motor_company=None, watt=None, location=None, **kwargs):
    try:
        if item_name == 운반비:
            price_dict = calculate_moveprice(location=location, size=size, quantity=quantity)
            unit_price = price_dict.get('UNIT', 0)
            return unit_price

        elif item_name == 조립인건비:
            return calculate_assembly_price(size, spec)

        elif item_name == 포장팔렛트:
            return calculate_pack_price(size, spec)

        elif item_name == NCT_가공비:
            return calculate_nct_price(size, spec)

        elif item_name == 볼트:
            return calculate_volt_price(size, spec)

        elif item_name == 자재비:
            return calculate_materialcost_price(size, spec)

        elif item_name == 도장비:
            return calculate_paint_price(size, spec)

        elif item_name == 포장용잡자재:
            return calculate_jab_price(size, spec)
            
        elif item_name == MOTOR:
            return calculate_motor_price(size, spec, motortype=motortype, motor_company=motor_company, watt=watt)
        
        elif item_name == 컨트롤러:
            return calculate_controller_price(size, spec, motortype=motortype, motor_company=motor_company, watt=watt)

        elif item_name == FAN:
            return calculate_fan_price(size, spec, motortype=motortype)
            
        elif item_name == BELLMOUTH:
            return calculate_bellmouth_price(size, spec, motortype=motortype)

        else:
            return 0

    except Exception as e:
        print(f"Error occurred at {item_name}: {e}")

# calculate_transportation 함수 수정
def calculate_transportation(size, quantity, location):
    try:
        move_price_data = calculate_moveprice(location, size, quantity)
        car_count_by_size = move_price_data.get('car_count_by_size', {})
        car_price = move_price_data.get('car_price', 0)

        one_carnum = car_count_by_size.get('one_carnum', 0)
        five_carnum = car_count_by_size.get('five_carnum', 0)
        ele_carnum = car_count_by_size.get('ele_carnum', 0)

        transportation_info = f"1ton: {one_carnum}대, 5ton: {five_carnum}대, 11ton: {ele_carnum}대"
        transportation_unit_price = car_price  # 단가 정보 가져오기
        transportation_total_price = transportation_unit_price * (one_carnum + five_carnum + ele_carnum)  # 합계 계산

        return transportation_info, transportation_unit_price, transportation_total_price

    except Exception as e:
        print(f"Error occurred in calculate_transportation: {e}")
        return '', 0, 0


# INPUT에서의 변수

def ffuInput(request):
    if request.method == 'POST':
        # 기존 데이터 가져오기
        size = request.POST.get('size') or 'Unknown Size'
        spec = request.POST.get('spec')
        motortype = request.POST.get('motortype')
        motor_company = request.POST.get('motor_company')
        watt = request.POST.get('watt')
        businessOwner = request.POST.get('businessOwner', '')
        location = request.POST.get('location', '')

        request.session['size'] = size
        request.session['businessOwner'] = businessOwner
        request.session['motortype'] = motortype
        request.session['location'] = location

        quantity_str = request.POST.get('quantity', '1')
        try:
            quantity = int(quantity_str)
        except ValueError:
            quantity = 1

        # 운반비 계산
        move_price_data = calculate_moveprice(location, size, quantity)  # 이 함수가 calculate_carsize와 연계하여 운반비를 계산합니다

        transportation_info = f"1ton: {move_price_data['car_count_by_size']['one_carnum']}대, 5ton: {move_price_data['car_count_by_size']['five_carnum']}대, 11ton: {move_price_data['car_count_by_size']['ele_carnum']}대"
        transportation_unit_price = move_price_data['car_price']  # 계산된 운반비 단가
        transportation_total_price = transportation_unit_price # 계산된 운반비 합계

        names = [자재비, 도장비, NCT_가공비, MOTOR, 컨트롤러, FAN, BELLMOUTH, 볼트, 포장용잡자재, 조립인건비, 포장팔렛트]

        items = []
        for name in names:

            try:
                if name in [MOTOR, 컨트롤러]:
                    unit_price = get_price_for_item(name, size, spec, motortype=motortype, motor_company=motor_company, watt=watt)
                elif name in [FAN, BELLMOUTH]:
                    unit_price = get_price_for_item(name, size, spec, motortype=motortype)
                elif name == 운반비:
                    unit_price = get_price_for_item(name, size, spec, quantity=quantity, location=location)
                else:
                    unit_price = get_price_for_item(name, size, spec)

                unit_price = round(unit_price)
                total_price = unit_price * quantity                         # 합계 = 단가 * 수량
                items.append((name, quantity, unit_price, total_price))     # 품명, 수량, 단가, 합계

                # transportation_info, transportation_unit_price, transportation_total_price = calculate_transportation(size, quantity, location)
                move_price_data = calculate_moveprice(location, size, quantity)
                transportation_info = f"1ton: {move_price_data['car_count_by_size']['one_carnum']}대, 5ton: {move_price_data['car_count_by_size']['five_carnum']}대, 11ton: {move_price_data['car_count_by_size']['ele_carnum']}대"
                transportation_unit_price = move_price_data['car_price']  # 계산된 운반비 단가
                transportation_total_price = transportation_unit_price  # 계산된 운반비 합계

                
            except Exception as e:
                print(f"Error occurred at {name}: {e}")  # 로깅을 위한 출력

        subtotal_unit = sum([item[2] for item in items])  # UNIT 소계 단가
        subtotal_totals = sum([item[3] for item in items])  # UNIT 소계 합계
        
        request.session['items'] = items

        load_data = calculate_carsize(size, quantity)       # ea 나중에 삭제

        context = {
            'items': items,
            'subtotal_unit': subtotal_unit,
            'subtotal_totals': subtotal_totals,
            'transportation_info': transportation_info,
            'transportation_unit_price': transportation_unit_price,
            'transportation_total_price': transportation_total_price,
            'load_data': load_data,
            'businessOwner': businessOwner,
            'location': location,
        }

        return render(request, 'FFUOutput.html', context)

    return render(request, 'FFUInput.html')


def ffuOutput(request):
    return render(request, 'FFUOutput.html')

def ffuDashboard(request):
    return render(request, 'FFUDashboard.html')    




