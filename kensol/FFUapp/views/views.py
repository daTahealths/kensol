from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
import tempfile
from django.views.decorators.http import require_POST

# 필요한 다른 import문들
from FFUapp.models.models import Estimate
import os
import pandas as pd

def get_context_from_size(size):
    quantity = 100
    unit_prices = []

    if size == "1200*1200":
        unit_prices = [1000] * 10

    totals = [price * quantity for price in unit_prices]
    subtotal_unit = sum(unit_prices)
    subtotal_totals = sum(totals)

    names = ['자재비 (AL, SPCC 외)', '도장비', 'NCT 판금 가공비', 'MOTOR & 컨트롤러', 'FAN', 'BELLMOUTH (보호망포함)', '볼트', '포장용 잡자재', '조립인건비', '포장팔렛트', '운반비']
    
    items = list(zip(names, unit_prices, totals))
    context = {'items': items, 'subtotal_unit': subtotal_unit, 'subtotal_totals': subtotal_totals}

    return context

def ffuInput(request):
    return render(request, 'FFUInput.html')

def ffuOutput(request):
    return render(request, 'FFUOutput.html')

def ffuCalculate(request):
    size = request.POST.get('size')
    context = get_context_from_size(size)
    return render(request, 'FFUOutput.html', context)