import rdflib
import networkx as nx
from pyvis.network import Network


rdf_file_path = 'materialized-triples.rdf'
g = rdflib.Graph()
g.parse(rdf_file_path, format="xml")  # Adjust the format based on your RDF file format


nx_graph = nx.Graph()

for triple in g:
    nx_graph.add_node(triple[0])
    nx_graph.add_node(triple[2])
    nx_graph.add_edge(triple[0], triple[2], label=triple[1])


net = Network(notebook=True)
net.from_nx(nx_graph)
net.show('rdf_visualization.html')