from django.shortcuts import render
from FFUapp.models.Assembly_models import GenAssembly, HighAssembly

def calculate_assembly_price(size, spec):
    """
    주어진 size와 spec에 따라 조립 가격을 반환합니다.
    """ 
    try:    
        if spec == "일반사양":
            model = GenAssembly
        elif spec == "고사양":
            model = HighAssembly
        else:
            return 0

        assembly = model.objects.filter(size=size).first()
        if assembly:
            return assembly.assembly_price 
        else:
            return 0  
        
    except Exception as e:
        print(f"Error occurred: {e}")  # 로깅을 위한 출력
        return 0