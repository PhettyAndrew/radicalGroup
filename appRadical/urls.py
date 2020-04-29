from django.urls import path
from . import views

app_name = 'appRadical'

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about, name='about'),
]
