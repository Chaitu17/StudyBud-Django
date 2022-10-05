from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "Home"),
    path('rooms/<str:pk>/', views.rooms, name = "Rooms"),
    path('create-room/', views.createRoom, name = "create-room"),
]