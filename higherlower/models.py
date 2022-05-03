from django.db import models


class Movie(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    review = models.DecimalField(max_digits=3, decimal_places=1)


class Scores(models.Model):
    score = models.PositiveSmallIntegerField()
    user = models.CharField(max_length=200)
    type = models.CharField(max_length=200)


class TvShow(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    review = models.DecimalField(max_digits=3, decimal_places=1)
