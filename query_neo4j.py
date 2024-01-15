from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI
from decouple import config
SECRET_KEY = config('SECRET_KEY')

ontology_file = 'ontology.owl'

graph = Neo4jGraph(
    url="bolt://34.237.220.249:7687", username="neo4j", password="armaments-influences-default"
)

chain = GraphCypherQAChain.from_llm(
    ChatOpenAI(temperature=0,api_key=SECRET_KEY), graph=graph, verbose=True, ontology_file=ontology_file,
)

result = chain.run('''Given the TTL file:
Write a SQL query that answers the question. The data for your query is available in a SERVICE identified by
<mapped>. Do not explain the query. return just the query, so it can be run verbatim from your response.
Here’s the question:
"generate a sql query to find all the entries in authentication_User''')

# Given the database described by the following DDL:
# INSERT SQL DDL
# Write a SQL query that answers the following question. Do not explain the query. return just the query, so it can be run
# verbatim from your response.
# Here’s the question:
# "INSERT QUESTION"

# Given the OWL model described in the following TTL file:
# INSERT OWL ontology
# Write a SQL query that answers the question. The data for your query is available in a SERVICE identified by
# <mapped>. Do not explain the query. return just the query, so it can be run verbatim from your response.
# Here’s the question:
# "generate a sql query to find all the entries in authentication_User"

# Given the TTL file:
# Write a SQL query that answers the question. The data for your query is available in a SERVICE identified by
# <mapped>. Do not explain the query. return just the query, so it can be run verbatim from your response.
# Here’s the question:
# "generate a sql query to find all the entries in authentication_User"


print(result)