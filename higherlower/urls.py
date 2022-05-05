from django.urls import path
from . import views

urlpatterns = [
    path('higherlower/movie', views.movie_higherlower),
    path('higherlower/show', views.show_higherlower),
    path('lost/<str:content>', views.lost),
    path('leaderboard/<str:content>', views.leaderboard)
]
