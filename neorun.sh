docker run \
    --name cranky_fermi \
    --restart unless-stopped \
    -p7474:7474 -p7687:7687 \
    -d \
    -v $HOME/neo4j/data:/data \
    -v $HOME/neo4j/logs:/logs \
    -v $HOME/neo4j/import:/var/lib/neo4j/import \
    -v $HOME/neo4j/conf:/var/lib/conf \
    neo4j/neo4j-arm64-experimental:4.3.1-arm64
