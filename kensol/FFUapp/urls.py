from django.urls import path
from FFUapp.views import command_views  # FFUapp/views 폴더 내의 views.py 가져오기

urlpatterns = [
    path('FFUInput/', command_views.ffuInput),
    path('FFUOutput/', command_views.ffuOutput),
    path('FFUDashboard/', command_views.ffuDashboard),
    path('download_excel/', command_views.download_excel, name='download_excel'),
]
