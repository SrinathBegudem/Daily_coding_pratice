"""
- Graph Basics in Python - Quick Overview
📌 What is a Graph?
A graph is a collection of:

Nodes/Vertices (points)
Edges (connections between points)

Example:
    1 --- 2
    |     |
    3 --- 4

Nodes: 1, 2, 3, 4
Edges: (1,2), (1,3), (2,4), (3,4)

- Types of graph representations
1) adjacent list : list of lists (For each node, store a list of its neighbors.)
# Using Dictionary
graph = {
    1: [2, 3],      # Node 1 connects to 2 and 3
    2: [1, 4],      # Node 2 connects to 1 and 4
    3: [1, 4],
    4: [2, 3]
}

# Using List (if nodes are 0 to n-1)
graph = [
    [1, 2],         # Node 0 connects to 1, 2
    [0, 3],         # Node 1 connects to 0, 3
    [0, 3],         # Node 2 connects to 0, 3
    [1, 2]          # Node 3 connects to 1, 2
]
2) Edge list
# List of tuples/lists
edges = [
    [1, 2],
    [1, 3],
    [2, 4],
    [3, 4]
]

# Or
edges = [(1,2), (1,3), (2,4), (3,4)]
3. Adjacency Matrix
# 2D array: matrix[i][j] = 1 if edge exists
graph = [
    [0, 1, 1, 0],   # Node 0: connects to 1, 2
    [1, 0, 0, 1],   # Node 1: connects to 0, 3
    [1, 0, 0, 1],   # Node 2: connects to 0, 3
    [0, 1, 1, 0]    # Node 3: connects to 1, 2
]

# Check if edge exists: graph[i][j] == 1


- Directed vs Undirected
# Undirected (both directions)
graph = {
    1: [2, 3],
    2: [1, 4],    # 2 includes 1 (bidirectional)
    3: [1, 4],
    4: [2, 3]
}

# Directed (one direction only)
graph = {
    1: [2, 3],    # 1 → 2, 1 → 3
    2: [4],       # 2 → 4 (no edge back to 1)
    3: [4],
    4: []         # No outgoing edges
}
"""
# Version 1: Dictionary-Based Graph Class for undirected graph 

class Graph:
    # lets intialize a empty graph 
    def __init__(self):
        self.graph = {}
    
    #add funcitonalities 

    #1) add nodes 
    def add_node(self,node):
        #check if the node is not already in graph 
        if not self.node_exist(node):
            self.graph[node] = []
        else:
            print(f"{node} node already exisits")


    #2) add edges btw 2 given nodes 
    def add_edge(self,u,v):
        #check if u and v node exisits, if not add then to avoid key not found error
        if not self.node_exist(u):
            self.add_node(u)  
        if not self.node_exist(v):
            self.add_node(v)
        
        #now once we made sure that the bot hnodes exisits lets add an edge
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    #3) return all neighbors of a given node 
    def get_neighbors(self,node):
        # check if node exist 
        if self.node_exist(node):
            return self.graph[node]
        #else return empty list
        return []

    #4) check if a node exists 
    def node_exist(self,node):
        if node in self.graph:
            return True
        else:
            return False
    
    #5) check if given two nodes has edge 
    def has_edge(self,u,v):
        #check if any one node exist either u or v as it is undirected graph 
        if self.node_exist(u): # if u exist let proceed to check if there is v in u val list 
            return v in self.graph[u] # if exist then true else 
        #if u didnt exisit then it sure that there is no edge even if v exist
        return False
    
    #6) get degree (no of connections) of a node
    def get_degree(self,node):
        #check if node exists 
        if self.node_exist(node):
            return len(self.graph[node])
        return f"{node} node doesn't exisit"
    
    #7) get all nodes
    def get_all_nodes(self):
        return list(self.graph.keys())
    
    def __str__(self):
        return str(self.graph)
    






