from django.urls import path, include
from . import views 

urlpatterns =[
    path('refresh/', views.refresh, name='refresh'),
    path('evaluate/', views.evaluate, name='evaluate'),
    path('', views.home, name='home')
]