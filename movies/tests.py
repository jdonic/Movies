from django.test import TestCase
from .models import Actor, Movie


class MovieTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.actor_1 = Actor.objects.create(name="Tom Hanks")
        cls.actor_2 = Actor.objects.create(name="Karel Roden")
        cls.movie_1 = Movie.objects.create(title="Muzi v nadeji")
        cls.movie_2 = Movie.objects.create(
            title="Zeny v nadeji",
        )
        cls.movie_1.actors.set([cls.actor_1, cls.actor_2])
        cls.movie_2.actors.set([cls.actor_1])

    def test_actor_name(self) -> None:
        self.assertEqual(f"{self.actor_1}", "Tom Hanks")
        self.assertEqual(self.actor_1.name, "Tom Hanks")
        self.assertEqual(f"{self.actor_2}", "Karel Roden")
        self.assertEqual(self.actor_2.name, "Karel Roden")

    def test_actor_movies(self) -> None:
        self.assertEqual(self.actor_1.movies.count(), 2)
        self.assertEqual(self.actor_2.movies.count(), 1)
        self.assertIn(self.movie_1, self.actor_1.movies.all())
        self.assertIn(self.movie_2, self.actor_1.movies.all())
        self.assertIn(self.movie_1, self.actor_2.movies.all())

    def test_movie_title(self) -> None:
        self.assertEqual(f"{self.movie_1}", "Muzi v nadeji")
        self.assertEqual(self.movie_1.title, "Muzi v nadeji")
        self.assertEqual(f"{self.movie_2}", "Zeny v nadeji")
        self.assertEqual(self.movie_2.title, "Zeny v nadeji")

    def test_movie_actors(self) -> None:
        self.assertEqual(self.movie_1.actors.count(), 2)
        self.assertEqual(self.movie_2.actors.count(), 1)
        self.assertIn(self.actor_1, self.movie_1.actors.all())
        self.assertIn(self.actor_2, self.movie_1.actors.all())
        self.assertIn(self.actor_1, self.movie_2.actors.all())

    def test_movie_detail_view(self) -> None:
        response = self.client.get("/movie_detail/1/")
        no_response = self.client.get("/movie_detail/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Muzi v nadeji")
        self.assertContains(response, "Karel Roden")
        self.assertTemplateUsed(response, "movies/movie_detail.html")

    def test_actor_detail_view(self) -> None:
        response = self.client.get("/actor_detail/1/")
        no_response = self.client.get("/actor_detail/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Tom Hanks")
        self.assertContains(response, "Muzi v nadeji")
        self.assertContains(response, "Zeny v nadeji")
        self.assertTemplateUsed(response, "movies/actor_detail.html")
