from django.shortcuts import render
from .models import Movie, Desired
from django.views.generic.base import View
from django.shortcuts import redirect



class MowiesViewDesired(View):
    
    def get(self, request):
        movie = request.user.desired.all()
        return render(request, template_name="movie_desired.html", context={"movie_desired":movie})


class AddDesired(View):

    def post(self, request, pk):
        movie = Movie.objects.get(id=pk)
        Desired.objects.create(user=request.user, movie=movie)
        return redirect('desired/')
