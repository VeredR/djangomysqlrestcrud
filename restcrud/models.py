from django.db import models



class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    user_score = models.IntegerField()
    overview = models.CharField(max_length=500)
    image = models.ImageField()

    class Meta:
        db_table = "movie"

    def __str__(self):
        return self