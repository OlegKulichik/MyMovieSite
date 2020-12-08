from django.urls import path
from . import views
from .views import MowiesView, AddStarRating


urlpatterns = [
    path("", views.MowiesView.as_view(), name="home"),
    path("search/", views.Search.as_view(), name='search'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
]