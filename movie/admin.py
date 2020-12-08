from django.contrib import admin
from .models import Movie, Category, Genre, RatingStar


admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(RatingStar)

