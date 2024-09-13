import argparse
from rdflib import Graph, URIRef

def filter_out_relations(graph_file, relations, filter_file=None):
    # Load the original graph
    graph = Graph()
    graph.parse(graph_file, format='turtle')

    # Load relations from file if specified
    if filter_file:
        with open(filter_file, 'r') as f:
            relations = f.read().splitlines()

    # Filter out specified relations
    for relation in relations:
        relation_uri = URIRef(relation)
        print("Removing " + relation_uri)
        graph.remove((None, URIRef(relation), None))

    # Save the filtered graph
    filtered_graph_file = graph_file.replace('.ttl', '_filtered.ttl')
    graph.serialize(filtered_graph_file, format='turtle')

    print(f"Filtered graph saved to {filtered_graph_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Filter out relations from an RDF graph')
    parser.add_argument('graph_file', help='Path to the original graph file')
    parser.add_argument('relations', nargs='+', help='Relations to filter out')
    parser.add_argument('-f', '--filterFile', help='Path to a file containing relations to filter out')
    args = parser.parse_args()

    filter_out_relations(args.graph_file, args.relations, args.filterFile)