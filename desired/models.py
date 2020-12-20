from django.db import models
from movie.models import Movie
from django.contrib.auth.models import User

class Desired(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", related_name="desired", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name="Фильм", related_name="desired", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie}"


    class Meta:
        unique_together = (('movie'),)
        verbose_name = "Желаемое"
        verbose_name_plural = "Желаемые"
