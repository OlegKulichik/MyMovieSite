from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.shortcuts import redirect
from .models import Movie, Category, Genre
import random



class GenreYearCategory:

    def get_genres(self):
        return Genre.objects.all()
    
    def get_category(self):
        return Category.objects.all()

    def get_years(self):
        return Movie.objects.all().values("year").distinct("year")
    

class MoviesView(GenreYearCategory, ListView):

    model = Movie
    queryset = Movie.objects.all()
    template_name="movie_list.html"
    paginate_by = 6


class LastMoviesView(GenreYearCategory, ListView):
    
    model = Movie
    queryset = Movie.objects.order_by("-id")[:5]
    template_name="movie_new.html"
    paginate_by = 3

class MovieDetailView(GenreYearCategory, DetailView):

    model = Movie
    queryset = Movie.objects.all()
    slug_field = "url"
    template_name="movie_detail.html"
    
class Search(GenreYearCategory, ListView):
    
    paginate_by = 1
    template_name="movie_list.html"
    
    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get("q"))


class FilterMoviesView(GenreYearCategory, ListView):

    template_name="movie_list.html"
    paginate_by = 3

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year"))|
            Q(genres__in=self.request.GET.getlist("genre"))|
            Q(category__in=self.request.GET.getlist("category"))
        ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        context["category"] = ''.join([f"category={x}&" for x in self.request.GET.getlist("category")])
        return context

class RandomMovies(View):

    def get(self, request):
        movie = Movie.objects.all()
        random_item = random.choice(movie)
        return render(request, template_name="movie_random.html", context={'random_item':random_item})
