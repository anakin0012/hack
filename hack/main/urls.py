from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('cn',views.main_view, name='main_cn'),
]
