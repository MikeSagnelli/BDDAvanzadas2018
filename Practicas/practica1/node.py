class Node():
    def __init__(self, name):
        self.visited = False
        self.neighbors = {}
        self.name = name
    
    def to_string(self):
        return str(self.name)

    def add_neighbor(self, node, weight):
        self.neighbors[node.name] = [weight, node]