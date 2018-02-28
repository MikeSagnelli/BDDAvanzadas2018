from node import Node

class Graph():
    def __init__(self):
        self.nodes = {}
        self.size = 0

    def add_node(self, node):
        self.nodes[node.name] = node
        self.size += 1
