from django.urls import path
from . import views

urlpatterns = [
    path('higherlower/movie/<str:content>', views.movie_higherlower),
    path('higherlower/show/<str:content>', views.show_higherlower),
    path('lost/<str:content>', views.lost),
    path('leaderboard/<str:content>', views.leaderboard)
]
