# Django Movies Project

This Django project scraps the [csfd](https://www.csfd.cz/zebricky/filmy/nejlepsi/) website for the top 300 best rated movies and their respective actors, stores them in the database and lets user search for the strings. The app then display all the movies and actors who have the string as part of their name and lets user to get to the detailed page
of the movie/actor by clicking on their name.


## Prerequisites
- [docker](https://docs.docker.com/engine/install/)
- [docker-compose](https://docker-docs.netlify.app/compose/install/#install-compose)
- [tox](https://pypi.org/project/tox/#description) (optional, for running tests and linters)

## Running the Project
Build the Docker images and run the containers:

`docker-compose up -d --build`

The database is present in the repository with all it's contents. You do not have to apply migrations.

However if you would like to, there is a script for scraping data from the web and populating the db.
For executing delete first the db.sqlite3 file, then apply migrations:

`docker-compose exec web python manage.py migrate`

Then you can execute the script for populating database, you can set the number of movies you want to scrape in constants.py.
`docker-compose exec web python manage.py populate_db`

After that, you can access the application in [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

To run the tests and linters execute:

`tox`