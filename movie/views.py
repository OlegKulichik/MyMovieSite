from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.shortcuts import redirect
from .models import Movie



class MoviesView(View):
     
    paginate_by = 1

    def get(self, request):
        movie = Movie.objects.all()
        return render(request, "movie_list.html", context={"movie_list":movie})

class MovieDetailView(View):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        return context

    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, template_name="movie_detail.html", context={"movie": movie})


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


class Search(View):
    
    paginate_by = 3

    def get(self, request):
        movie = Movie.objects.filter(title__icontains=self.request.GET.get("q"))
        return  render(request, "movie_list.html", context={"movie_list":movie})

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["q"] = f'q={self.request.GET.get("q")}&'
    #     return context