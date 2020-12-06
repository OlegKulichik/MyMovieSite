from django.contrib import admin
from .models import Movie, Category, Genre, Reviews, RatingStar,Desired


admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Reviews)
admin.site.register(RatingStar)
admin.site.register(Desired)

