from django.core.management.base import BaseCommand
from movies.models import Actor, Movie
from movies.scrape_movies import scrape_csfd_movies
from movies.constants import MOVIES_COUNT

from typing import Any


class Command(BaseCommand):
    help = "Populate the database with films and actors"

    def handle(self, *args: Any, **options: Any) -> None:
        films_actors = scrape_csfd_movies(MOVIES_COUNT)
        for film_actors in films_actors:
            film, _ = Movie.objects.get_or_create(
                id=film_actors["movie_id"], title=film_actors["title"]
            )
            for actor in film_actors["actors"]:
                actor_obj, _ = Actor.objects.get_or_create(
                    id=actor["actor_id"], name=actor["name"]
                )
                film.actors.add(actor_obj)
