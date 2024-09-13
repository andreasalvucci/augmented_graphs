import sys
from rdflib import Graph

def merge_graphs(graphs, output_file):


    merged_graph = Graph()
    
    for graph_file in graphs:
        graph = Graph()
        

        graph.parse(graph_file, format='turtle')
        for prefix, uri in graph.namespaces():
            merged_graph.bind(prefix, uri)
        merged_graph += graph
    
    merged_graph.serialize(destination=output_file, format='turtle')
    try:
        parsed_graph = Graph()
        parsed_graph.parse(data=merged_graph.serialize(format='turtle'), format='turtle')
        print("Graph syntax is valid.")
    except Exception as e:
        print("Graph syntax error:", str(e))
    
    

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python merge_graphs.py <graph1> <graph2> ... <output_file>")
        sys.exit(1)
    
    graphs = sys.argv[1:-1]
    output_file = sys.argv[-1]
    
    merge_graphs(graphs, output_file)