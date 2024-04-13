from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('movies/', views.movie_listing, name='movie_listing'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('show/<int:show_timing_id>/booking/', views.booking, name='booking'),
    path('booking/history/', views.booking_history, name='booking_history'),
]
