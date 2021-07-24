from pandas.io.pytables import incompatibility_doc
from cypher_utils import *
from bs4 import BeautifulSoup
from neo4j import GraphDatabase

uri = "bolt://cranky_fermi:7687"

driver = GraphDatabase.driver(uri, auth=('neo4j', 'oscarfelix'), encrypted=False)

  
# Reading data from the xml file 
df = pd.DataFrame(read_clz_xml("movie_2021-07-24_18-20-18-export.xml"))
df.columns = ('title', 'upc', 'imdburl', 'coverfront', 'coverback')
print(df.shape)
print(df.head())

dfdicts = df.to_dict(orient='records')


for x in dfdicts:
    imdb_url = x['imdburl']
    if imdb_url:
    # print(set_movie_attrs(imdb_url, x))
        with driver.session() as sess:
            sess.run(set_movie_attrs(imdb_url, x))

