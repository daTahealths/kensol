from django.shortcuts import render
from FFUapp.models.Move_models import LoadQuantity, LocationMovecost
from collections import defaultdict

def calculate_carsize(size, quantity):
    try:
        load_data_qs = LoadQuantity.objects.filter(size=size)
        
        load_data = defaultdict(int)
        for item in load_data_qs:
            carsize = item.carsize
            ea = item.ea
            load_data[carsize] = ea
        
        one_carnum, five_carnum, ele_carnum = 0, 0, 0 

        one_ton_ea = load_data['1ton']
        five_ton_ea = load_data['5ton']
        eleven_ton_ea = load_data['11ton']

        # 조건에 따른 차량 대수 계산
        if quantity >= eleven_ton_ea:
            ele_carnum = quantity // eleven_ton_ea
            remainder = quantity % eleven_ton_ea

            if remainder > five_ton_ea:
                ele_carnum += 1
            elif remainder > one_ton_ea:
                five_carnum += 1
            else:
                one_carnum += 1

        elif quantity > five_ton_ea:
            ele_carnum += 1
        elif quantity > one_ton_ea:
            five_carnum += 1
        else:
            one_carnum += 1

        return {
            'one_carnum': one_carnum,
            'five_carnum': five_carnum,
            'ele_carnum': ele_carnum,
        }

    except Exception as e:
        print(f"Error occurred in calculate_carsize: {e}")
        return {'one_carnum': 0, 'five_carnum': 0, 'ele_carnum': 0}



def calculate_moveprice(location, size, quantity):
    try:
        loc_data_qs = LocationMovecost.objects.filter(location=location)
        
        # 각 carsize의 move_price를 저장할 딕셔너리 초기화
        move_price_data = {}
        for item in loc_data_qs:
            # 데이터베이스에서 가져온 정보를 로드합니다.
            carsize = item.carsize
            move_price = item.move_price

            # 가져온 정보를 move_price_data 딕셔너리에 저장합니다.
            move_price_data[carsize] = move_price

        # 각 carsize의 move_price를 변수에 저장
        elemove_price = move_price_data.get('11ton', 0)
        fivemove_price = move_price_data.get('5ton', 0)
        onemove_price = move_price_data.get('1ton', 0)

        # calculate_carsize 함수에서 각 carsize의 carnum을 가져온다
        carsize_count = calculate_carsize(size, quantity)

        # 각 carsize의 carprice를 계산한다
        elecarprice = elemove_price * carsize_count['ele_carnum']
        fivecarprice = fivemove_price * carsize_count['five_carnum']
        onecarprice = onemove_price * carsize_count['one_carnum']

        # 최종 운반비를 계산한다
        car_price = elecarprice + fivecarprice + onecarprice

        return {
            'car_price': car_price,
            'car_count_by_size': carsize_count
        }

    except Exception as e:
        print(f"Error occurred in calculate_moveprice: {e}")
        return {'car_price': 0, 'car_count_by_size': {}}
