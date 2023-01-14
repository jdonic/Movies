import requests
from bs4 import BeautifulSoup

from movies.constants import BASE_URL


def scrape_csfd_movies(movies_count: int) -> list:

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 \
        (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15"
    }

    movies: list = []

    # iterate over the 4 pages
    for i in range(4):
        url = BASE_URL + "/zebricky/filmy/nejlepsi/?from={}".format(i * 100)
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")

        movie_containers = soup.find_all("article", class_="article")

        # extract the movie names and links
        for container in movie_containers:
            if len(movies) < movies_count:
                name = container.find("a", class_="film-title-name").text.strip()
                link = BASE_URL + container.find("a", class_="film-title-name")["href"]
                movie_page = requests.get(link, headers=headers)
                movie_soup = BeautifulSoup(movie_page.text, "html.parser")
                creators = movie_soup.find_all("div", class_="creators")
                actors_list = []
                for creator in creators:
                    h4 = creator.find_all("h4")
                    for h4_tag in h4:
                        if h4_tag.text.strip() == "Hrají:":
                            parent_div = h4_tag.find_parent()
                            actors = parent_div.find_all("a")
                            actors_list += [actor.text for actor in actors]
                            if actors_list[-1] == "více":
                                actors_list.pop()
                            break
                movies.append({"name": name, "actors": actors_list})
            else:
                break

    return movies
