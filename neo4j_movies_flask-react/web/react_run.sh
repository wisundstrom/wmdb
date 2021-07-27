#!/bin/bash

docker run -t -d \
	-p 3000:3000 \
	--restart unless-stopped \
	-e REACT_APP_API_BASE_URL='https://willsundstrom.com:443/api/v0' \
       	--network wmdb \
	wmdb:dev

