from graph import Graph
from node import Node
import csv

NODE_TO_START = "511108000000000"

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

# bfs = graph.breadth_first_search(NODE_TO_START)
dfs = graph.depth_first_search(NODE_TO_START)

# print ("There are %s nodes after Breadth-First algorithm" % (len(bfs)))
# for vertex in bfs:
#     print(vertex.to_string())
print ("There are %s nodes after Depth-First algorithm" % (len(dfs)))
for vertex in dfs:
    print(vertex.to_string())