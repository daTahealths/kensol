from django.urls import path
from FFUapp.views import views  # FFUapp/views 폴더 내의 views.py 가져오기

urlpatterns = [
    path('FFUInput/', views.ffuInput),      # 'ffuInput/' : 웹페이지 URL에서 ffuInput/ | # views.ffuInput : 앞서 import한 views.py의 ffuInput 함수 
    path('FFUOutput/', views.ffuOutput),
    path('ffuCalculate/', views.ffuCalculate),
    path('convert_to_pdf/', views.convert_to_pdf, name='convert_to_pdf'),
]