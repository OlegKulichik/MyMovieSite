from django.urls import path
from . import views
from .views import MowiesView, MowiesViewDesired,register,user_login,user_logout, AddStarRating


urlpatterns = [
    path("", views.MowiesView.as_view(), name="home"),
    path('register/', register, name = 'register'),
    path('login/', user_login, name = 'login'),
    path('logout/', user_logout, name = 'logout'),
    path("search/", views.Search.as_view(), name='search'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path("<int:pk>", views.AddDesired.as_view(),name="add_desired"),
    path("<int:pk>", views.AddReview.as_view(), name="add_review"),
    path("desired/", views.MowiesViewDesired.as_view(), name="movie_desired"),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
]