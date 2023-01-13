# movies/urls.py
from django.urls import path
from .views import MovieDetailView


urlpatterns = [
    path("movie_detail/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
]
