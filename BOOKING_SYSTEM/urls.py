from django.urls import path
from . import views 
from django.contrib import admin

urlpatterns = [
    path("", views.index_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name="login"),
    path('booking/', views.booking_view, name="booking"),
    path('booking/confirmation/<int:booking_id>/', views.booking_confirmation_view, name='booking_confirmation'),
    
    path('availabledate/add-dates/', views.add_dates_view, name='add-dates'),
]
