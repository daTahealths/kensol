from django.shortcuts import render

# 메인 페이지 HTML 추가 예정
def home(request):
    return render(request, 'index.html')