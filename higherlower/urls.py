from django.urls import path
from . import views

urlpatterns = [
    path('higherlower/<str:content>', views.higherlower),
    path('lost/<int:score>', views.lost)
]
