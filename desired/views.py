from django.shortcuts import render
from .models import Desired
from django.views.generic.base import View
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from movie.views import GenreYearCategory
from movie.models import Movie


class MowiesViewDesired(View):
    
    def get(self, request):
        movie = request.user.desired.all()
        return render(request, template_name="movie_desired.html", context={"movie_desired":movie})


class AddDesired(View):

    def post(self, request, pk):
        movie = Movie.objects.get(id=pk)
        Desired.objects.create(user=request.user, movie=movie)
        return redirect(movie.get_absolute_url())
