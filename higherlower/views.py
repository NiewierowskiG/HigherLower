from django.shortcuts import render, redirect
import imdb
import random
from .models import Movie

def lost(request, score):
    return render(request, "higherlower/lost.html", {'score': score})


def higherlower(request,content):
    if content == 'new':
        queryset = Movie.objects.filter(title__endswith='Dances with Wolves')#last title in Top250
        if not queryset.exists():
            print(queryset)
            ia = imdb.IMDb()
            Top250Movies = ia.get_top250_movies()
            for movie in Top250Movies:
                movietmp = ia.get_movie(movie.movieID)
                Movie.objects.create(url=f"{movietmp['cover url'].split('_V1_', 1)[0]}.jpg", review=movietmp['rating'], title=movietmp['title'])
        movie1 = Movie.objects.filter(id=random.randint(1, 250))
        movie2 = Movie.objects.filter(id=random.randint(1, 250))
        score = 0
    else:
        tmp = content.split(';')
        score = int(tmp[1])
        if int(tmp[0]) == 0:
            return redirect(f'/lost/{score}')
        score += 1
        movie1 = Movie.objects.filter(id=tmp[2])
        movie2 = Movie.objects.filter(id=random.randint(1, 250))
    if float(movie1[0].review) > float(movie2[0].review):
        higher = 0
        lower = 1
    elif float(movie1[0].review) < float(movie2[0].review):
        higher = 1
        lower = 0
    else:
        higher = 1
        lower = 1
    context = {'movie1': movie1[0], 'movie2': movie2[0], 'score': score, 'higher': higher, 'lower': lower}
    return render(request, "higherlower/higherlower.html", context)
