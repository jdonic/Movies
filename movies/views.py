from django.views.generic import DetailView

from .models import Movie, Actor


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"


class ActorDetailView(DetailView):
    model = Actor
    template_name = "movies/actor_detail.html"
