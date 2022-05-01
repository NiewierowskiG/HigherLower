from django.urls import path
from . import views

urlpatterns = [
    path('higherlower/<str:content>', views.higherlower),
    path('lost/<str:content>', views.lost),
    path('leaderboard/<str:content>', views.leaderboard)
]
