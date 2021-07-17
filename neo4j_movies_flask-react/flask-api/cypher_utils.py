from neo4j import GraphDatabase
import pandas as pd
import numpy as np
import string

def node_feat(row):
    pairstrings = []
    for x in row.items():
        feat = x[0].replace(" ","_")
        val = x[1]
        if x[1] == 'null':
            strin = f"{feat}:{val}"
        elif isinstance(x[1], str):
            val = val.replace('"',"")
            strin = f'{feat}:"{val}"'
        else:
            strin = f"{feat}:{val}"

        pairstrings.append(strin)

    dictstring = ", ".join(pairstrings)
    return dictstring

def create_movie( movie):
    return "CREATE (%s:Movie {%s, %s})" % (
        movie['Title'].lower().translate(str.maketrans('', '', string.punctuation)).replace(" ","_"),
        f"""name:"{movie['Title']}", id:apoc.create.uuid() """, 
        node_feat(movie))


def node_list(row, col):
    plist = row[col].split(", ")
    return plist

def merge_nonmovie_query(col, edge, num_nodes, node_type='person'):  
    
    mmatch = "MATCH (m:Movie {Title:$movie})"
    pmatch = [mmatch]
    attach = []
    gmatch = []
    attach2 = []

    #this should be nodes everywhere instead of peeps, but i just dont want to do that.
    peeps = [f"{node_type}_{x}" for x in range(num_nodes)]
    
    for peep in peeps:
        pmatch.append("MERGE (%s:%s {name:%s})" % (peep, node_type.title() , "$"+peep))
        pmatch.append("ON CREATE SET %s.id = apoc.create.uuid()" % (peep))
        
        if node_type == 'person':
            attach.append("MERGE (m)<-[:%s]-(%s)" % (edge, peep))
            attach.append("SET %s : %s" % (peep, col))
        else:
            attach.append("MERGE (m)-[:%s]->(%s)" % (edge, peep))

    merges = " \n".join(pmatch + attach )
    return merges


def node_args(row, col, node):
    pl = node_list(row, col)
    peeps = [f"{node}_{x}" for x in range(len(pl))]
    peep_dict = dict(zip(peeps, pl))
    return peep_dict


def merge_nodes(driver, row, col, edge, node_type='person'):
    
    num_nodes = len(node_list(row,col))
    
    query_template = merge_nonmovie_query(col, edge, num_nodes, node_type)

    node_dict = node_args(row, col, node_type)
    
    try:
        with driver.session() as session:
            result = session.run(query_template,
                                movie=row['Title'],
                                **node_dict
                                )
    except Exception as e:
        print(e)
        assert False, f"""
            row: {row}, col: {col}, edge: {edge}, node:{node_type}, num_nodes:{num_nodes} \n
            node_dict: {node_dict} \n
            query_template: {query_template}
            """


