from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="HOME"),
    path('room/<str:pk>', views.room, name="ROOM"),
]


