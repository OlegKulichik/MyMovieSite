from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import Movie, Desired
from .forms import ReviewForm, UserRgisterForm, UserLoginForm

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
        movie = request.user.desired.all()
        print(movie)
        return render(request, template_name="movie_desired.html", context={"movie_desired":movie})

class MovieDetailView(View):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        return context

    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, template_name="movie_detaill.html", context={"movie": movie})

class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save() 
        return redirect(movie.get_absolute_url())

class AddDesired(View):

    def post(self, request, pk):
        movie = Movie.objects.get(id=pk)
        Desired.objects.create(user=request.user, movie=movie)
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

class Search(ListView):
    paginate_by = 3

    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context