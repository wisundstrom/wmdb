docker run -it \
	-restart unless-stopped \
       	--network wmdb \
       	--volume=/home/pi/wmdb-project/wmdb/neo4j_movies_flask-react/flask-api:/app \
       	--name stupefied_engelbart \ 
	flask_backend:prod 
