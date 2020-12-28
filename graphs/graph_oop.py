# Graph - With Object-Oriented Adjacency List Implementation

# Support for directed, weighted edges
# Vertices stored in an adjacency matrix

class Graph():
    def __init__(self, adj, w=[]):
        self.adj = adj # Adjacency list - INPUT VERTICES only
        # self.d = [] # List of shortest-path distance estimates for each vertex `v` in `V`
        # self.p = [] # List of predecessors
        self.w = w # List of weights for edges - INPUT WEIGHTS only
        # self.V = [v for v in range(0, len(G.adj))]

        self.new_adj = self.intialize_adj_u() # Alternative implementation.


    def print_graph(self):
        """
        Prints graph as adjacency list
        """
        print("----Printing graph----")

        for u in range(0, len(self.new_adj)):
            print(f"new_adj[{u}]: {self.new_adj[u][0].u} \nd[{u}]: {self.new_adj[u][0].d}", end="\n")
            print(f"p[{u}]: {self.new_adj[u][0].p}\n--------")
                
        return

    def vertex_exist(self, s):
        """
        Answers if vertex `s` exists in `V`
        """
        if s >= len(self.adj) or s < 0:
            raise Exception("Error: Invalid source vertex `s`")
            return False

        # If source vertex exists, and has edges to other vertices
        if self.adj[s] != None:
            return True

        return False

    def init_ss(self, s): # "init_single_source"
        """
        Initialize distance estimates `d[u]` to +infinity for all `u`
        """
        # self.d = [float("+inf") for u in self.adj]
        self.new_adj[s][0].d = 0 # Source dist is initially 0
        # self.p = [-1 for u in self.adj] # All predecessors set to 1 intially (unused for BFS or DFS)
        return
    
    def relax(self, u, v):
        """
        "Relaxes" the distance estimate for edge (u, v)
        if the old weight `w` is greater than the calculated
        cost d[u] + w[(u, v)].
        Where `u` is a potentially "better (lower cost)" predecessor to `v`
        OOP Implementation:
        `u` is a Vertex.u - NOT THE OBJECT ITSELF
        `v` is a ListVertex.v
        """
        # We know u, but we need to traverse the list to get `v`
        # Since vertex `v` is not neccessarily at position G.adj[u][v] in the adj. list of vertex `u`
        # print(f"HEY: u = {u}, v = {v}, d[u] = {self.d[u]}, d[v] = {self.d[v]}")
        # print(self.adj[u])
        v_idx_in_w = self.get_new_adj_idx(u, v)
        print(u)

        # If the old cost is worse than the new cost
        # print(f"{self.d[v]} > {self.d[u]} + {self.w[u][v_idx_in_w]} is {self.d[v] > self.d[u] + self.w[u][v_idx_in_w]}")
        if self.new_adj[v][0].d > self.new_adj[u][0].d + self.new_adj[u][v_idx_in_w].w:
            # print(f"UPDATE d[v]: {self.d[v]}")
            self.new_adj[v][0].d = self.new_adj[u][0].d + self.new_adj[u][v_idx_in_w].w
            self.new_adj[v][0].p = u # Set a new best-predecessor
        # print(f"Final d[v]: {self.d[v]}")
        return

    def get_adj_idx(self, u, v):
        """
        For searching the input array `adj`
        O(n) lookup in a linked list adj[u], at position adj[u][v_idx_in_w], where its value is `v`
        """
        for _v in range(0, len(self.adj[u])):
            # print(_v)
            # print(self.adj[u][_v])
            if self.adj[u][_v] == v: # Found location # was u - will need for relax...
                return _v # set index to be used for self.w[u][v]
        raise Exception(f"Error: Could not locate v = {v}'s index in adj[{u}]")
        return -1 
    
    def get_new_adj_idx(self, u, v):
        """
        For searching list vertices in `new_adj        
        O(n) lookup in a linked list adj[u], at position adj[u][v_idx_in_w], where its value is `v`
        `u` is a Vertex.u - NOT THE OBJECT ITSELF
        `v` is a ListVertex.v
        """
        for _v in range(1, len(self.new_adj[u])): # Begin at 1 since ListVertices begin after 0
            # print(_v)
            # print(self.new_adj[u][_v])
            if self.new_adj[u][_v].v == v: # Found location # was u - will need for relax...
                return _v # set index to be used for self.w[u][v]
        raise Exception(f"Error: Could not locate v = {v}'s index in adj[{u}]")
        return -1 
    
    def intialize_adj_u(self):
        """
        UNUSED - likely not to be implemented due to complexity. This
        was just an experimental more-object-oriented approach.
        Builds new_adj list (this is a different take on the 
        adjacency list, with v, w, d, and p values included).
        """
        # Initialize vertices `u`
        new_adj = [[] for i in range(0, len(self.adj))]

        # Initialize vertices `v`
        for u in range(0, len(self.adj)):
            new_adj[u].append(Vertex(u)) # Note: in this format, the vertex `u` is at index 0 of each list, and ListVertices `v` follow from index 1 onwards.
            # print(new_adj)
            # Add adjacent ListVertices `v` for each `u`
            for v in self.adj[u]:
                # print(f"{u}, {v}")
                v_idx_in_w = self.get_adj_idx(u, v)
                new_adj[u].append(ListVertex(v, self.w[u][v_idx_in_w]))
        print(new_adj)
        return new_adj

# Alternative method to store vertex objects in new_adj list
class Vertex():
    # This is for vertex `u` in G.adj - may need one consistent name (u or v) if want to use in algos.
    def __init__(self, u, d = float("+inf"), p = -1):
        self.u = u # Vertex Key
        self.d = d # Distance Estimate
        self.p = p # Predecessor vertex key
    
    def __repr__(self):
        return f"Vertex({self.u}, {self.d}, {self.p})"

class ListVertex():
    # For vertices `v` of an edge(u, v), with weight `w`
    # (ListVertex is for all vertices `v` in G.adj[u]'s list)
    def __init__(self, v, w, d = float("+inf")):
        self.v = v # Vertex Key
        self.w = w # Weight of edge(u, v)
        self.d = d # Distance Estimate - NOTE: This is unideal. `d` should be kept an external array to save space.
    
    def __repr__(self):
        return f"ListVertex({self.v}, {self.w}, {self.d})"
    
class Queue():
    def __init__(self):
        self.q = []

    def enqueue(self, v):
        """
        Add a node/vertice `v` to the front of the queue.
        """
        self.q.insert(0, v)
        return

    def dequeue(self):
        """
        Pop a node/vertice from the end of the queue, and return vertex.
        """
        return self.q.pop(-1)