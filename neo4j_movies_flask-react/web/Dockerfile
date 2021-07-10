# pull official base image
FROM node:12.22.3-alpine

# set working directory
WORKDIR /app


# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

#get correct node sass binary
#COPY ./sass/linux-x64-72_binding.node ./sass/linux-x64-72_binding.node
#ENV SASS_BINARY_PATH=./sass/linux-x64-72_binding.node

#Build and install nodesass locally
#COPY ./sass ./sass/
#WORKDIR ./sass
#RUN npm install --unsafe-perm -g .
#npm --ignore-scripts false rebuild --build-from-source node-sass --sass-binary-site=http://localhost:0




#COPY node_modules/node-sass/vendor/linux-arm64-72/binding.node /app/binding.node
#ENV SASS_BINARY_PATH=./node_modules/node-sass/vendor/linux-arm64-72/binding.node

#WORKDIR /app/node_modules/node-sass
#RUN npm install -g .

#RUN npm --ignore-scripts false rebuild --build-from-source node-sass --sass-binary-path=./node_modules/node-sass/vendor/linux-arm64-72/binding.node

#WORKDIR /app


# install app dependencies
COPY package.json ./
#COPY package-lock.json ./


RUN apk add --update --no-cache python2 && ln -sf python2 /usr/bin/python
RUN apk add --update make && apk add --update g++

RUN npm install
#RUN npm install node-sass --sass-binary-path=/app/binding.node

#RUN npm rebuild node-sas --sass-binary-path=/app/binding.node

RUN npm install react-scripts@3.4.1 -g

# add app
COPY . . 

#COPY app.json ./
#COPY src/ ./src/
#COPY public/ ./public/
#COPY static.json ./
#COPY .nvmrc ./

#RUN npm install node-sass --sass-binary-path=./node_modules/node-sass/vendor/linux-arm64-72/binding.node 

# start app
CMD ["npm", "start"]
#CMD ["sh"]

