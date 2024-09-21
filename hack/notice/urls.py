from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice_list, name='notice_list'),
    path('cn',views.notice_list_cn, name='notice_list_cn'),
]
