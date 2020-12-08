from django.urls import path
from . import views
from .views import AddReview


urlpatterns = [
    path("<int:pk>", views.AddReview.as_view(), name="add_review"),
]