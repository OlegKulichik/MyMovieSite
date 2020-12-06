from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login, logout

from .models import Movie
from .forms import DesiredForm, ReviewForm, UserRgisterForm, UserLoginForm

def register(request):
    if request.method == "POST":
        form = UserRgisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserRgisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')

class MowiesView(View):
    
    def get(self, request):
        movie = Movie.objects.all()
        return render(request, template_name="movie_list.html", context={"movie_list":movie})

class MowiesViewDesired(View):
    
    def get(self, request):
        movie = Movie.objects.filter(draft=True)
        return render(request, template_name="movie_desired.html", context={"movie_desired":movie})

class MovieDetailView(View):

    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, template_name="movie_detail.html", context={"movie": movie})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        return context

class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        print(request.user.email)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save() 
        return redirect(movie.get_absolute_url())

class AddDesired(View):

    def post(self, request, pk):
        form = DesiredForm(request.POST)
        movie = Movie.objects.get(id=pk)
        movie.draft = True
        movie.save()
        return redirect('/')


class AddStarRating(View):
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)