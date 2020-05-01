from django.urls import path
from . import views

app_name = 'appRadical'

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about, name='about'),
    path('building_plan', views.plan, name='building'),
    path('building_plan/code:<int:building_id>/', views.building_details, name='building_details'),
    path('contact_us', views.contact, name='contact'),
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('building_plan/online/lipa:<int:purchase_id>/purchase/', views.lipa_na_mpesa_online, name='purchase'),
]
