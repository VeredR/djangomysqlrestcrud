from datetime import datetime, timedelta

from django.db import models


class Movies(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    release_date = models.DateField()
    score = models.IntegerField()
    overview = models.CharField(max_length=500)
    image = models.URLField()

    class Meta:
        db_table = "movies"

    def __str__(self):
        return self


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=60)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self


class Rentals(models.Model):

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Users,  on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    ttl = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = "rentals"

    def __str__(self):
        return self
