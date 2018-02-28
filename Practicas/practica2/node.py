class Node():
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.linking_neighbors = {}
        self.page_rank = 0.0
        self.c = 0
    
    def to_string(self):
        return str(self.name)

    def add_neighbor(self, node, weight):
        self.neighbors[node.name] = [weight, node]
        node.linking_neighbors[self.name] = self
        self.c = self.c + 1

    def update_page_rank(self, d):
        i = 0
        for node in self.linking_neighbors.values():
            i = i + (node.page_rank / node.c)
        self.page_rank = (1 - d) + (d * i)