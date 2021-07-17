from neo4j import GraphDatabase
import pandas as pd
import numpy as np
import string
from itertools import product

from cypher_utils import *


from neo4j import GraphDatabase

uri = "bolt://cranky_fermi:7687"

driver = GraphDatabase.driver(uri, auth=('neo4j', 'oscarfelix'), encrypted=False)
#this is to wipe all data before adding movies
with driver.session() as session:
    result = session.run("MATCH ()-[e]-() delete e")
    result = session.run("MATCH (n) delete n")
    result = session.run("CALL apoc.schema.assert({}, {})")
    
    result = session.run("MATCH (a) RETURN a limit 5")
print(result.data())


#setup constraints/indices
def unique_builder(label, prop):
    return "CREATE CONSTRAINT ON (n:%s) ASSERT n.%s IS UNIQUE;" % (label, prop)

constraints = [
    unique_builder(label, prop) 
    for label, prop in product([ "Person", "Movie", "Genre"],["uuid", "Name"])
    ]
    

with driver.session() as session:
    for con in constraints:
        print(con)
        session.run(con)
    
print("Done!")

