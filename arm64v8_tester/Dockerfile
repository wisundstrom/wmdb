FROM arm64v8/ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev
  
RUN apt-get install -y iputils-ping && \
   apt-get install -y dnsutils

RUN pip install --no-cache-dir neo4j py2neo requests pandas

CMD [ "bash" ]
