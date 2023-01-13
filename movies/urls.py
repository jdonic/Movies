# movies/urls.py
from django.urls import path
from .views import MovieDetailView, ActorDetailView


urlpatterns = [
    path("movie_detail/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
    path("actor_detail/<int:pk>/", ActorDetailView.as_view(), name="actor_detail"),
]
