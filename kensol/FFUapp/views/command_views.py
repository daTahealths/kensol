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
from .FFilter_views import calculate_ffilter_price

자재비 = "자재비 (AL, SPCC 외)"
도장비 = "도장비"
NCT_가공비 = "NCT 가공비"
MOTOR = "MOTOR"
컨트롤러 = "컨트롤러"
FAN = "FAN"
BELLMOUTH = "BELLMOUTH (보호망포함)"
볼트 = "볼트&리벳"
필터 = "FILTER"
포장용잡자재 = "포장용 잡자재"
조립인건비 = "조립인건비"
포장팔렛트 = "포장팔렛트"
운반비 = "운반비"
일반사양 = "일반사양"
고사양 = "고사양"


# OUTPUT 항목과 연관된 변수
def get_price_for_item(item_name, size, spec, ph, quantity=None, motortype=None, location=None, filterpressure=None, filterstyle=None, **kwargs):
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
            price_dict = calculate_nct_price(size, spec)
            unit_price = price_dict.get('UNIT', 0)
            return unit_price

        elif item_name == 볼트:
            return calculate_volt_price(size, spec)

        elif item_name == 자재비:
            return calculate_materialcost_price(size, spec)

        elif item_name == 도장비:
            return calculate_paint_price(size, spec)

        elif item_name == 포장용잡자재:
            return calculate_jab_price(size, spec)
            
        elif item_name == MOTOR:
            return calculate_motor_price(size, spec, motortype=motortype, ph=ph)
        
        elif item_name == 컨트롤러:
            return calculate_controller_price(size, spec, motortype=motortype, ph=ph)

        elif item_name == FAN:
            return calculate_fan_price(size, spec, motortype=motortype)
            
        elif item_name == BELLMOUTH:
            return calculate_bellmouth_price(size, spec, motortype=motortype)
        
        elif item_name == 필터:
            return calculate_ffilter_price(size, filterstyle=filterstyle, filterpressure=filterpressure)

        else:
            return 0

    except Exception as e:
        print(f"Error occurred at {item_name}: {e}")

# INPUT에서의 변수
def ffuInput(request):
    if request.method == 'POST':
        # 기존 데이터 가져오기
        size = request.POST.get('size') or 'Unknown Size'
        spec = request.POST.get('spec')
        motortype = request.POST.get('motortype')
        ph = request.POST.get('ph')
        businessOwner = request.POST.get('businessOwner', '')
        location = request.POST.get('location', '')
        maintenance = request.POST.get('maintenance', '1')
        operating_profit = request.POST.get('operating_profit', '1')
        filterstyle = request.POST.get('filterstyle')
        filterpressure = request.POST.get('filterpressure')
        quantity_str = request.POST.get('quantity', '1')
        try:
            quantity = int(quantity_str)
        except ValueError:
            quantity = 1

        request.session['size'] = size
        request.session['businessOwner'] = businessOwner
        request.session['motortype'] = motortype
        request.session['location'] = location
        request.session['quantity'] = quantity

        # 운반비 단가, 합계 계산
        move_price_data = calculate_moveprice(location, size, quantity)
        move_price_data_rounded = {key: round(value) if isinstance(value, (int, float)) else value for key, value in move_price_data.items()}
        transportation_total_price = move_price_data_rounded['car_price']

        # NCT 단가, 합계 계산
        nct_unit_price = round(calculate_nct_price(size, spec))
        nct_total_price = nct_unit_price * quantity

        # 포장팔렛트 단가, 합계 계산
        pack_unit_price = round(calculate_pack_price(size, spec))
        pack_total_price = pack_unit_price * quantity

        # 조립인건비 단가, 합계 계산
        assembly_unit_price = round(calculate_assembly_price(size, spec))
        assembly_total_price = assembly_unit_price * quantity

        # 포장용잡자재 단가, 합계 계산
        jab_unit_price = round(calculate_jab_price(size, spec))
        jab_total_price = jab_unit_price * quantity

        # 볼트 단가, 합계 계산
        volt_unit_price = round(calculate_volt_price(size, spec))
        volt_total_price = volt_unit_price * quantity

        # 도장비 단가, 합계 계산
        paint_unit_price = round(calculate_paint_price(size, spec))
        paint_total_price = paint_unit_price * quantity
        
        # 자재비 단가, 합계 계산
        materialcost_unit_price = round(calculate_materialcost_price(size, spec))
        materialcost_total_price = materialcost_unit_price * quantity

        # 모터 단가, 합계 계산
        motor_unit_price = round(calculate_motor_price(size, spec, motortype=motortype, ph=ph))
        motor_total_price = motor_unit_price * quantity

        # 컨트롤러 단가, 합계 계산
        controller_unit_price = round(calculate_controller_price(size, spec, motortype=motortype, ph=ph))
        controller_total_price = controller_unit_price * quantity

        # FAN 단가, 합계 계산
        fan_unit_price = round(calculate_fan_price(size, spec, motortype=motortype))
        fan_total_price = fan_unit_price * quantity

        # BELLMOUTH 단가, 합계 계산
        bellmouth_unit_price = round(calculate_bellmouth_price(size, spec, motortype=motortype))
        bellmouth_total_price = bellmouth_unit_price * quantity

        # FILTER 단가, 합계 계산
        ffilter_unit_price = round(calculate_ffilter_price(size, filterstyle=filterstyle, filterpressure=filterpressure))
        ffilter_total_price = ffilter_unit_price * quantity

        # 합계 계산
        subtotal_unit = nct_unit_price + pack_unit_price + assembly_unit_price + jab_unit_price + volt_unit_price + paint_unit_price + materialcost_unit_price + motor_unit_price + controller_unit_price + fan_unit_price + bellmouth_unit_price + transportation_total_price
        subtotal_totals = quantity * (nct_unit_price + pack_unit_price + assembly_unit_price + jab_unit_price + volt_unit_price + paint_unit_price + materialcost_unit_price + motor_unit_price + controller_unit_price + fan_unit_price + bellmouth_unit_price) + transportation_total_price

        # 직접비 계산
        direct_unit = ffilter_unit_price + subtotal_unit
        direct_totals = ffilter_total_price + subtotal_totals

        # 간접비 계산

        try:
            maintenance = float(maintenance)
        except ValueError:
            maintenance = 1.0  # 디폴트 값 설정
        
        try:
            operating_profit = float(operating_profit)
        except ValueError:
            operating_profit = 1.0  # 디폴트 값 설정

        maintenance_unit = round(direct_unit * (maintenance/100))                  # 관리비 단가
        operating_profit_unit = round(direct_unit * (operating_profit/100))        # 영업이익 단가         
        maintenance_totals = maintenance_unit * quantity                           # 관리비 합계
        operating_profit_totals = operating_profit_unit * quantity                 # 영업이익 합계
        indirect_totals = maintenance_totals + operating_profit_totals             # 간접비 합계
    

        # 총계
        aggregate_unit = direct_unit + maintenance_unit + operating_profit_unit    # 총계 단가
        aggregate_totals = direct_totals + indirect_totals                         # 총계 합계

        load_data = calculate_carsize(size, quantity)

        context = {
            'subtotal_unit': subtotal_unit,
            'subtotal_totals': subtotal_totals,
            'transportation_total_price': transportation_total_price,
            'load_data': load_data,
            'businessOwner': businessOwner,
            'location': location,
            'size': size,
            'motortype': motortype,
            'quantity': quantity,
            'nct_unit_price' : nct_unit_price,
            'nct_total_price' : nct_total_price,
            'pack_unit_price' : pack_unit_price,
            'pack_total_price' : pack_total_price,
            'assembly_unit_price' : assembly_unit_price,
            'assembly_total_price' : assembly_total_price,
            'jab_unit_price' : jab_unit_price,
            'jab_total_price' : jab_total_price,
            'volt_unit_price' : volt_unit_price,
            'volt_total_price' : volt_total_price,
            'paint_unit_price' : paint_unit_price,
            'paint_total_price' : paint_total_price,
            'materialcost_unit_price' : materialcost_unit_price,
            'materialcost_total_price' : materialcost_total_price,
            'motor_unit_price' : motor_unit_price,
            'motor_total_price' : motor_total_price,
            'controller_unit_price' : controller_unit_price,
            'controller_total_price' : controller_total_price,
            'fan_unit_price' : fan_unit_price,
            'fan_total_price' : fan_total_price,
            'bellmouth_unit_price' : bellmouth_unit_price,
            'bellmouth_total_price' : bellmouth_total_price,
            'ffilter_unit_price' : ffilter_unit_price,
            'ffilter_total_price' : ffilter_total_price,
            'direct_unit' : direct_unit,
            'direct_totals' : direct_totals,
            'maintenance_unit' : maintenance_unit,
            'operating_profit_unit' : operating_profit_unit,
            'maintenance_totals' : maintenance_totals,
            'operating_profit_totals' : operating_profit_totals,
            'indirect_totals' : indirect_totals,
            'aggregate_unit' : aggregate_unit,
            'aggregate_totals' : aggregate_totals,
        }

        # Excel로 불러내기 위해 변수 저장
        # unit_price
        request.session['materialcost_unit_price'] = materialcost_unit_price
        request.session['paint_unit_price'] = paint_unit_price
        request.session['nct_unit_price'] = nct_unit_price
        request.session['motor_unit_price'] = motor_unit_price
        request.session['controller_unit_price'] = controller_unit_price
        request.session['fan_unit_price'] = fan_unit_price
        request.session['bellmouth_unit_price'] = bellmouth_unit_price
        request.session['volt_unit_price'] = volt_unit_price
        request.session['jab_unit_price'] = jab_unit_price
        request.session['assembly_unit_price'] = assembly_unit_price
        request.session['pack_unit_price'] = pack_unit_price
        request.session['ffilter_unit_price'] = ffilter_unit_price
        request.session['direct_unit'] = direct_unit
        request.session['maintenance_unit'] = maintenance_unit
        request.session['operating_profit_unit'] = operating_profit_unit
        request.session['aggregate_unit'] = aggregate_unit

        # total_price
        request.session['materialcost_total_price'] = materialcost_total_price
        request.session['paint_total_price'] = paint_total_price
        request.session['nct_total_price'] = nct_total_price
        request.session['motor_total_price'] = motor_total_price
        request.session['controller_total_price'] = controller_total_price
        request.session['fan_total_price'] = fan_total_price
        request.session['bellmouth_total_price'] = bellmouth_total_price
        request.session['volt_total_price'] = volt_total_price
        request.session['jab_total_price'] = jab_total_price
        request.session['assembly_total_price'] = assembly_total_price
        request.session['pack_total_price'] = pack_total_price
        request.session['transportation_total_price'] = transportation_total_price
        request.session['ffilter_total_price'] = ffilter_total_price
        request.session['direct_totals'] = direct_totals
        request.session['maintenance_totals'] = maintenance_totals
        request.session['operating_profit_totals'] = operating_profit_totals
        request.session['aggregate_totals'] = aggregate_totals

        request.session['subtotal_unit'] = subtotal_unit
        request.session['subtotal_totals'] = subtotal_totals

        return render(request, 'FFUOutput.html', context)

    return render(request, 'FFUInput.html')

def ffuOutput(request):
    return render(request, 'FFUOutput.html')

def ffuDashboard(request):
    return render(request, 'FFUDashboard.html')    