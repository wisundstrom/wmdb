# wmdb
Wills Movie Database is a graph database powered analytics and visualization project for your movie collection.

##### UPDATE: This project took a sharp left turn, moving to a RaspberryPi 4 instead of aws

This eliminated the various problems that arise from aws and replaced them with the problems of getting all this code to run on ARM64

The current plan is that this app is going to be running in three docker containers in a docker network, which eventually be connected to an NGINX reverse proxy (maybe containerized IDK yet) and opened up to the world wide web.

I'm using this wonderful template and guide from the folks at neo4j for skeleton of the app: https://neo4j.com/developer/python-movie-app/


- **Graph Database:** For the moment I'm using just using the arm64 image from neo4j:`Neo4j/neo4j-arm64-experimental:4.3.1-arm64`. This, annoyingly, is the community version with a bunch of features paywalled. For the moment I'm working with between 0 and 3 total users, 100 movies, and 800 nodes / 1000 edges for the graph, so I'll be able to get by with the fre version. Now that OngDB 1.0 is out I may try to switch over at some point, but having to compile everything from source to get it to run on arm64 sounds like a huge pain.

- **App Backend:** The python-flask backend docker container and code are in the [flask-api directory](https://github.com/wisundstrom/wmdb/tree/main/neo4j_movies_flask-react/flask-api), and I am [using this guide](https://docs.docker.com/language/python/build-images/) to dockerize the flask app. The flask-api is mostly working, the schema of the data coming out of the movie db I'm using needs to be matched up with the api a little better. This is also where any other miscellaneous python code will be executed from, like the selenium webscraper that dowloads and imports the movie data.

- **App Fronted:** A react app that hooks into the api from the flask container. This is what needs the most work at the moment, it hasn't really been changed from the template, other than to get the app compiled and working on arm64. The react app sends requests to the flask api but the formatting and a bunch of hard-coded demo examples in the template need to be fixed
