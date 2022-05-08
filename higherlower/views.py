from django.shortcuts import render, redirect
import imdb
import random
from .models import Movie, Scores, TvShow


def set_higher_and_lower(review1, review2):
    if float(review1) > float(review2):
        higher = 0
        lower = 1
    elif float(review1) < float(review2):
        higher = 1
        lower = 0
    else:
        higher = 1
        lower = 1
    return higher, lower


def lost(request, content):
    tmp = content.split(';')
    Scores.objects.create(score=int(tmp[1]), user=request.user.username, type=tmp[0])
    return render(request, "higherlower/lost.html", {'score': tmp[1]})


def show_higherlower(request):
    if request.GET.get('clicked'):
        score = int(request.GET.get('score'))
        if int(request.GET.get('correct')) == 0:
            Scores.objects.create(score=score, user=request.user.username, type="show")
            return render(request, "higherlower/lost.html", {'score': score, "type": "show"})
        score += 1
        shows = list(TvShow.objects.all())
        show1 = TvShow.objects.get(id=request.GET.get('movie_id'))
    else:
        queryset = TvShow.objects.filter(id=1)
        if not queryset.exists():
            ia = imdb.IMDb()
            top_250_shows = ia.get_top250_tv()
            for show in top_250_shows:
                movietmp = ia.get_movie(show.movieID)
                TvShow.objects.create(url=f"{movietmp['cover url'].split('_V1_', 1)[0]}.jpg", review=movietmp['rating'],
                                      title=movietmp['title'])
        shows = list(TvShow.objects.all())
        show1 = random.choice(shows)
        score = 0
    show2 = random.choice(shows)
    higher, lower = set_higher_and_lower(show1.review, show2.review)
    context = {'movie1': show1, 'movie2': show2, 'score': score, 'higher': higher, 'lower': lower, 'type': "show"}
    return render(request, "higherlower/higherlower.html", context)


def movie_higherlower(request):
    if request.GET.get('clicked'):
        score = int(request.GET.get('score'))
        if int(request.GET.get('correct')) == 0:
            Scores.objects.create(score=score, user=request.user.username, type="show")
            return render(request, "higherlower/lost.html", {'score': score, "type": "show"})
        score += 1
        movies = list(Movie.objects.all())
        movie1 = TvShow.objects.filter(id=(request.GET.get('movie_id')))
    else:
        queryset = Movie.objects.filter(id=1)  # last title in Top250
        if not queryset.exists():
            print(queryset)
            ia = imdb.IMDb()
            Top250Movies = ia.get_top250_movies()
            for movie in Top250Movies:
                movietmp = ia.get_movie(movie.movieID)
                Movie.objects.create(url=f"{movietmp['cover url'].split('_V1_', 1)[0]}.jpg", review=movietmp['rating'],
                                     title=movietmp['title'])
        movies = list(Movie.objects.all())
        movie1 = random.choice(movies)
        score = 0
    movie2 = random.choice(movies)
    higher, lower = set_higher_and_lower(movie1.review, movie2.review)
    context = {'movie1': movie1, 'movie2': movie2, 'score': score, 'higher': higher, 'lower': lower,
               'type': "movie"}
    return render(request, "higherlower/higherlower.html", context)


def leaderboard(request, content):
    highscores = Scores.objects.filter(type=content).order_by('-score')
    return render(request, "higherlower/leaderboard.html", {'highscores': highscores})
