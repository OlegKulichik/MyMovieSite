from django.shortcuts import render
from .forms import ReviewForm
from movie.models import Movie
from django.views.generic.base import View
from django.shortcuts import redirect

class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save() 
        return redirect(movie.get_absolute_url())
