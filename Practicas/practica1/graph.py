from node import Node

class Graph():
    def __init__(self):
        self.nodes = {}
        self.size = 0

    def add_node(self, node):
        self.nodes[node.name] = node
        self.size += 1

    def breadth_first_search(self, start):
        queue = [self.nodes[start]]
        self.nodes[start].visited = True
        visited = [self.nodes[start]]
        while queue:
            vertex = queue.pop(0)
            for node in vertex.neighbors.values():
                if node[1].visited == False:
                    queue.append(node[1])
                    visited.append(node[1])
                    node[1].visited = True
        
        return visited

        

    def depth_first_search(self, start):
        stack = [self.nodes[start]]
        self.nodes[start].visited = True
        visited = [self.nodes[start]]
        while stack:
            vertex = stack.pop()
            for node in vertex.neighbors.values():
                if node[1].visited == False:
                    stack.append(node[1])
                    visited.append(node[1])
                    node[1].visited = True
        
        return visited
