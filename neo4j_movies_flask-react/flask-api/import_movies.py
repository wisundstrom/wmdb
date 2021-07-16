from neo4j import GraphDatabase
import pandas as pd
import numpy as np
import string

from cypher_utils import *


from neo4j import GraphDatabase

uri = "bolt://192.168.1.203:7687"

driver = GraphDatabase.driver(uri, auth=('neo4j', 'oscarfelix'), encrypted=False)
with driver.session() as session:
    result = session.run("MATCH (a) RETURN a limit 5")
print(result.data())

df = pd.read_csv("export_movies.csv")
df.head()
df = df.fillna('null')

#this is to wipe all data before adding movies
with driver.session() as session:
    result = session.run("Match ()-[e]-() delete e")
    result = session.run("Match (n)delete n")
    result = session.run("MATCH (a) RETURN a limit 5")
print(result.data())

row_dicts = df.to_dict(orient='records')



for row in row_dicts:
    with driver.session() as sess:
        sess.run(create_movie(row))

with driver.session() as session:
    result = session.run("MATCH (a) RETURN count(a)")

print(result.data())

people_cols = ['Actor','Director', 'Musician', 'Photography', 'Producer', 'Writer']
edges = ["ACTED_IN", "DIRECTED", "MUSCIAN_IN", "PHOTOGRAPHY_FOR", "PRODUCED", "WROTE"]
role_zip = list(zip(people_cols, edges))
for row in row_dicts:
    for role in role_zip:
        merge_people(driver, row, role[0], role[1])
