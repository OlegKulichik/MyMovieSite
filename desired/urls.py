from django.urls import path
from . import views
from .views import  MowiesViewDesired, AddDesired

urlpatterns = [
    path("<int:pk>", views.AddDesired.as_view(),name="add_desired"),
    path("desired/", views.MowiesViewDesired.as_view(), name="movie_desired"),
]