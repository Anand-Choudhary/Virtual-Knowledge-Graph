from rdflib import Graph
import csv

def rdf_to_csv(rdf_file, csv_file):
    g = Graph()
    g.parse(rdf_file, format='ttl')  # Adjust the format based on your RDF file format

    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write header
        header = ['subject', 'predicate', 'object']
        csv_writer.writerow(header)

        # Write triples
        for triple in g:
            csv_writer.writerow([str(term) for term in triple])

if __name__ == "__main__":
    rdf_to_csv('mapping_r2rml.ttl', 'materialized-triples.csv')
