from django.urls import path
from . import views

urlpatterns = [
    path('cn', views.map_C_view, name='map_C'),
    path('',views.map_E_view, name='map_E'),
    path('jp',views.map_J_view, name='map_J'),
]
