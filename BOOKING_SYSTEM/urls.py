from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('booking/', views.booking_view, name="booking"),
    path('booking/confirmation/<int:booking_id>/', views.booking_confirmation_view, name='booking_confirmation'),
]