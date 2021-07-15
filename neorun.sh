
docker run \
    --name cranky_fermi \
    --restart unless-stopped \
    --network wmdb --network-alias neo_server \
    -p7474:7474 -p7687:7687 \
    -d \
    -v /home/pi/neo4j/data:/var/lib/neo4j/data \
    -v /home/pi/neo4j/logs:/logs \
    -v /home/pi/neo4j/import:/var/lib/neo4j/import \
    -v /home/pi/neo4j/conf:/var/lib/neo4j/conf \
    -e NEO4JLABS_PLUGINS=\[\"apoc\"\] \
    neo4j/neo4j-arm64-experimental:4.3.1-arm64
