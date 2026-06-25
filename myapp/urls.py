from django.urls import path
from myapp import views  # ✅ OK



urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('hotels/', views.hotel, name='hotel'),
    path('home/', views.home_view, name='home'),
    path('booking/', views.booking_view, name='booking'),
    path('hotel/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('booking/', views.booking_view, name='booking'),
    path('booking/<int:booking_id>/confirm/', views.booking_confirm, name='booking_confirm'),
    path('booking/<int:booking_id>/pdf/', views.booking_pdf, name='booking_pdf'),
]