# movies/urls.py
from django.urls import path
from .views import MovieDetailView, ActorDetailView, SearchListView


urlpatterns = [
    path("", SearchListView.as_view(), name="search_list"),
    path("movie_detail/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
    path("actor_detail/<int:pk>/", ActorDetailView.as_view(), name="actor_detail"),
]
