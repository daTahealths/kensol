from django.shortcuts import render
from calc.models import Estimate
import os
import pandas as pd

RESOURCES = 'D:\\jango\\resources'

# Create your views here.
def ffuInput(request):
    return render(request, 'ffuInput.html')

def ffuOutput(request):
    return render(request, 'ffuOutput.html')

def ffuCalculate(request):
    # 선택된 규격에 따른 단가들이 고정되는 부분
    size = request.POST.get('size') # ffuInput.html에서 선택된 'size'를 가져옵니다.
    quantity = 100
    unit_prices = []

    if size == "1200*1200":
        # 선택된 규격이 "1200*1200"인 경우, 각 항목의 단가를 1000으로 고정
        unit_prices = [1000] * 10  # 10개 항목에 대해 각각 1000으로 단가 설정
    
    # 합계 및 UNIT 소계 계산
    totals = [price * quantity for price in unit_prices]  # 각 항목에 대한 합계
    subtotal_unit = sum(unit_prices)  # UNIT 소계 (단가 합계)
    subtotal_totals = sum(totals)  # UNIT 소계 (합계 합계)

    # 이름 리스트 (화면에 표시하기 위해)
    names = ['자재비 (AL, SPCC 외)', '도장비', 'NCT 판금 가공비', 'MOTOR & 컨트롤러', 'FAN', 'BELLMOUTH (보호망포함)', '볼트', '포장용 잡자재', '조립인건비', '포장팔렛트', '운반비']
    
    # names, unit_prices, totals을 하나의 리스트로 묶기
    items = list(zip(names, unit_prices, totals))
    context = {'items': items, 'subtotal_unit': subtotal_unit, 'subtotal_totals': subtotal_totals}
    
    return render(request, 'ffuOutput.html', context)

# HTML to PDF   
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

def convert_to_pdf(request):
    # Render the HTML to a string
    template = render_to_string('your_template.html', context)

    # Create a temporary file to write the PDF to
    with tempfile.NamedTemporaryFile(delete=True) as output:

        # Convert the HTML to PDF
        HTML(string=template).write_pdf(output.name)

        # Read the PDF from the temporary file
        output.seek(0)
        pdf = output.read()

    # Create an HTTP response with the PDF file
    response = HttpResponse(pdf, content_type='application/pdf')

    # If you want the PDF to be downloaded, add this line
    response['Content-Disposition'] = 'attachment; filename="your_pdf_name.pdf"'

    return response
