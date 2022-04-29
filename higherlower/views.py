from django.shortcuts import render
import imdb
import random
from .models import Movie

def higherlower(request):
    queryset = Movie.objects.filter(title__endswith='Dances with Wolves')#last title in Top250
    if not queryset.exists():
        print(queryset)
        ia = imdb.IMDb()
        Top250Movies = ia.get_top250_movies()
        for movie in Top250Movies:
            movietmp = ia.get_movie(movie.movieID)
            Movie.objects.create(url=f"{movietmp['cover url'].split('_V1_', 1)[0]}.jpg", review=movietmp['rating'], title=movietmp['title'])
    context = {}
    return render(request, "higherlower/higherlower.html", context)
