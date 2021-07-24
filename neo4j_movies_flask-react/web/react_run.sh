#!/bin/bash

docker run -t -d \
	-p 3000:3000 \
	-e REACT_APP_API_BASE_URL='http://localhost:5000/api/v0' \
       	--network wmdb \
	wmdb:dev

