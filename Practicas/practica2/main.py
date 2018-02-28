from graph import Graph
from node import Node
import csv

D = 0.85
ITERATIONS = 5

graph = Graph()

with open('Nodes.csv') as nodes:
    read_nodes_csv = csv.reader(nodes, delimiter=',')
    for row in read_nodes_csv:
        if(row[0] != "Id"):
            graph.add_node(Node(row[0]))
    
with open('Edges.csv') as edges:
    read_edges_csv = csv.reader(edges, delimiter=',')
    for row in read_edges_csv:
        if(row[0] != "Source"):
            graph.nodes[row[0]].add_neighbor(graph.nodes[row[1]], row[2])

print ("There are %s nodes in the graph." % (graph.size))

for i in range(ITERATIONS):
    for key in graph.nodes.keys():
        graph.nodes[key].update_page_rank(D)

for key, value in sorted(graph.nodes.items(), key=lambda item: (item[1].page_rank, item[0])):
    print(str(value.name) + " has a rank of " + str(value.page_rank))