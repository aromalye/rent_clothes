from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('check_booking/<int:pk>/', views.check_bookings, name="check_booking"),
    path('create_booking/', views.create_booking, name="create_booking"),

]