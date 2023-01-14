from django.views.generic import DetailView, ListView

from itertools import chain

from .models import Movie, Actor
from django.db.models import Q


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"


class ActorDetailView(DetailView):
    model = Actor
    template_name = "movies/actor_detail.html"


class SearchListView(ListView):
    template_name = "movies/search_list.html"

    # overwriting the get_queryset function to customize the queryset
    def get_queryset(self) -> list:
        query = self.request.GET.get("q")
        if query:
            movies = Movie.objects.filter(Q(title__icontains=query))
            actors = Actor.objects.filter(Q(name__icontains=query))
            # use the chain function to combine the querysets
            return list(chain(movies, actors))
        else:
            # return an empty list if no query is provided
            return []
