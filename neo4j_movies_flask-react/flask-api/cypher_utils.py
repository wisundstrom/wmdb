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
        f"""name:"{movie['Title']}" """, 
        node_feat(movie))


def people_list(row, col):
    plist = row[col].split(", ")
    return plist

def merge_people_query(col, edge, num_peeps):  
    
    mmatch = "MATCH (m:Movie {Title:$movie})"
    pmatch = [mmatch]
    attach = []
    peeps = [f"person_{x}" for x in range(num_peeps)]
    
    for peep in peeps:
        pmatch.append("MERGE (%s:Person {name:%s})" % (peep, "$"+peep))
        attach.append("MERGE (m)<-[:%s]-(%s)" % (edge, peep))
        attach.append("SET %s : %s" % (peep, col))
    
    merges = " \n".join(pmatch + attach)
    return merges


def people_args(row, col):
    pl = people_list(row, col)
    peeps = [f"person_{x}" for x in range(len(pl))]
    peep_dict = dict(zip(peeps, pl))
    return peep_dict


def merge_people(driver, row, col, edge):
    
    num_people = len(people_list(row,col))
    query_template = merge_people_query(col, edge, num_people)
    peep_dict = people_args(row, col)
    
    with driver.session() as session:
        result = session.run(query_template,
                             movie=row['Title'],
                             **peep_dict
                            )