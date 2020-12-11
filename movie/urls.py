from django.urls import path
from . import views
from .views import MoviesView


urlpatterns = [
    path("", views.MoviesView.as_view(), name="home"),
    path("search/", views.Search.as_view(), name='search'),
    path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
]