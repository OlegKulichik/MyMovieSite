from django.urls import path
from . import views


urlpatterns = [
    path("", views.MoviesView.as_view(), name="home"),
    path("new/", views.LastMoviesView.as_view(), name="last_movie"),
    path("random/", views.RandomMovies.as_view(), name="random_movie"),
    path("search/", views.Search.as_view(), name='search'),
    path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
]