# pull official base image
FROM node:12.22.3-alpine

# set working directory
WORKDIR /app


# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./



RUN apk add --update --no-cache python2 && ln -sf python2 /usr/bin/python
RUN apk add --update make && apk add --update g++

RUN npm install


RUN npm install react-scripts@3.4.1 -g

# add app
COPY . . 

# start app
CMD ["npm", "start"]
#CMD ["sh"]

