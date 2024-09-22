from django.urls import path
from . import views

urlpatterns = [
    path('Emergency', views.Emergency_view, name='emergency_en'),
    path('Hospital', views.Hospital_view, name='hospital_en'),
    path('Hospital_cn', views.Hospital_cn_view, name='hospital_cn'),
    path('Hospital_jp', views.Hospital_jp_view, name='hospital_jp'),
    path('Mbank',views.Mbank_view, name='Mbank_en'),
    path('Mmobile',views.Mmobile_view, name='Mmobile_en'),
    path('Pt',views.Pt_view, name='Pt_en'),
    path('Waste',views.Waste_view, name='Waste_separation_en'),
]
