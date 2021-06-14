docker run -it \
--name ongdb \
-p7474:7474 -p7687:7687 \
--volume=$HOME/ongdb/data:/data \
graphfoundation/ongdb-enterprise:1.0
