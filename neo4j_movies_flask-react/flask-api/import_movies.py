import pandas as pd
import numpy as np
import string

from cypher_utils import *


from neo4j import GraphDatabase

uri = "bolt://cranky_fermi:7687"

driver = GraphDatabase.driver(uri, auth=('neo4j', 'oscarfelix'), encrypted=False)

df = pd.read_csv("clz_data/export_movies.csv")
df.sample(1).head()

df = df.fillna('null')

#this is to wipe all data before adding movies
with driver.session() as session:
    result = session.run("MATCH (a) RETURN count(a)")
print("node_count before", result.data())

row_dicts = df.to_dict(orient='records')



# for idx, row in enumerate(row_dicts):
#     print(f"Import movie row: {idx}")
#     with driver.session() as sess:
#         sess.run(create_movie(row))

people_cols = ['Genre','Actor','Director', 'Musician', 'Photography', 'Producer', 'Writer']
edges = ["IN_GENRE","ACTED_IN", "DIRECTED", "MUSCIAN_IN", "PHOTOGRAPHY_FOR", "PRODUCED", "WROTE"]
role_zip = list(zip(people_cols, edges))
for idx, row in enumerate(row_dicts):
    print(f"Import movie : {idx}")
    with driver.session() as sess:
        sess.run(create_movie(row))
    for role in role_zip:
        if role[0] == 'Genre':
            
            merge_nodes(driver, row, role[0], role[1], node_type='genre')
        else:
            
            merge_nodes(driver, row, role[0], role[1])


with driver.session() as session:
    result = session.run("MATCH (a) RETURN count(a)")
    print("node_count after",result.data())


