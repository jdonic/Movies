from django.views.generic import DetailView, ListView

from unidecode import unidecode
from itertools import chain

from .models import Movie, Actor


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
            movies = list(
                filter(
                    lambda x: unidecode(query.lower()) in unidecode(x.title).lower(),
                    Movie.objects.all(),
                )
            )
            actors = list(
                filter(
                    lambda x: unidecode(query.lower()) in unidecode(x.name).lower(),
                    Actor.objects.all(),
                )
            )
            # use the chain function to combine the querysets
            return list(chain(movies, actors))
        else:
            # return an empty list if no query is provided
            return []
