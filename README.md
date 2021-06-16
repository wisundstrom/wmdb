# wmdb
Wills Movie Database is a graph database powered analytics and visualization project for your movie collection.

I'm using this wonderful template and guide from the folks at neo4j for the web app part of the site: https://neo4j.com/developer/python-movie-app/

For now the aws setup for hosting all of this online has been configured via the aws website, eventually that workflow will be translated into some aws cli scripts that will live here
The basic idea of that setup is:
- A central efs [elastic file storage](https://aws.amazon.com/efs/) volume that will hold the actual ongdb database and whatever else needs non-ephemeral storage
- The ondgdb database running in a docker container on ecs [elastic container service](https://aws.amazon.com/ecs/), with the computing resources powered by [aws Fargate]() instead of a normal ec2 server. (I may have to switch to ec2 if fargate ends up being expensive, but it seems cool and ec2 is annoying, so I'm giving it a shot
- The python-flask backend of the web app will probably also be an ecs container on fargate, [using this guide to dockerize as flask app] (https://docs.docker.com/language/python/build-images/)
- Not sure how I'm going to run the frontend react app, probably another container, ecs seems to have robust ways to organize tasks and services that rely on multilple containers
- Not sure how I want to handle the data exports from the clz movies online app, at the moment I'm thinking something with [aws Lambda](https://aws.amazon.com/lambda/)
- Finally, going along with aws best practices, most of these containers and filessystem will live in a vpc without public IP's, so we use one of their load balancers (ugh) as a gateway to the wide open internet. [This guide on aws will have a bunch of useful stuff](https://aws.amazon.com/getting-started/hands-on/build-modern-app-fargate-lambda-dynamodb-python/module-two/)
 
