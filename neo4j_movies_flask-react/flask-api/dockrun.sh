docker run -it -p 5000:5000 --network wmdb --user="$(id -u)" --volume=$HOME/wmdb-project/wmdb/neo4j_movies_flask-react/docker_volume:/storage flask_backend:dev
