from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User




class Genre(models.Model):

    name = models.CharField("Имя", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Category(models.Model):

    name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Movie(models.Model):

    title = models.CharField(verbose_name="Название", max_length=100)
    tagline = models.CharField(verbose_name="Слоган", max_length=100, default='')
    description = models.TextField(verbose_name="Описание")
    poster = models.ImageField(verbose_name="Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField(verbose_name="Дата выхода", default=2019)
    country = models.CharField(verbose_name="Страна", max_length=30)
    directors = models.CharField(max_length=150, verbose_name="режиссер")
    actors = models.CharField(max_length=150, verbose_name="актеры")
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    world_premiere = models.DateField(verbose_name="Примьера в мире", default=date.today)
    budget = models.PositiveIntegerField(verbose_name="Бюджет", default=0, help_text="указывать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField(
        verbose_name="Сборы в США", default=0, help_text="указывать сумму в долларах"
    )
    fess_in_world = models.PositiveIntegerField(
        verbose_name="Сборы в мире", default=0, help_text="указывать сумму в долларах"
    )
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return f"{self.url}"

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})


    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

