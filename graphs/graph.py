# Graph

# Support for directed, weighted edges
# Vertices stored in an adjacency matrix

EMPTY = "EMPTY" # No vertex present

class Graph():
    def __init__(self, adj, w=[]):
        self.adj = adj # Adjacency list
        self.d = [] # List of shortest-path distance estimates for each vertex `v` in `V`
        self.p = [] # List of predecessors
        self.w = w # List of weights for edges
        # self.V = [v for v in range(0, len(G.adj))]

        # DFS-Specific
        self.colour = [] # Colour of vertices
        self.dt = [] # Discovery Time for vertices
        self.ft = [] # Finish Time for vertices
        self.time = -1

    def print_graph(self):
        """
        Prints graph as adjacency list.
        params: [bfs, dfs, bellman-ford, dijkstra]
        """
        print("----Printing graph----")

        for u in range(0, len(self.adj)):
            if u is not EMPTY:
                print("----", end="")
                self.print_val("adj", u, self.adj[u])
                if len(self.d) is not 0:
                    self.print_val("d", u, self.d[u])
                if len(self.p) is not 0:
                    self.print_val("p", u, self.p[u])
                if len(self.colour) is not 0:
                    self.print_val("colour", u, self.colour[u])
                if len(self.dt) is not 0:
                    self.print_val("dt", u, self.dt[u])
                if len(self.ft) is not 0:
                    self.print_val("ft", u, self.ft[u])
        if self.time is not -1:
            print("time: ", self.time)
        return
    
    def print_val(self, prefix, u, value):
        print(f"{prefix}[{u}]: {value}", end="\n")
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
        self.d = [float("+inf") for u in self.adj]
        self.d[s] = 0 # Source dist is initially 0
        self.p = [-1 for u in self.adj] # All predecessors set to 1 intially (unused for BFS or DFS)
        return
    
    def relax(self, u, v):
        """
        "Relaxes" the distance estimate for edge (u, v)
        if the old weight `w` is greater than the calculated
        cost d[u] + w[(u, v)].
        Where `u` is a potentially "better (lower cost)" predecessor to `v`
        """
        # We know u, but we need to traverse the list to get `v`
        # Since vertex `v` is not neccessarily at position G.adj[u][v] in the adj. list of vertex `u`
        # print(f"HEY: u = {u}, v = {v}, d[u] = {self.d[u]}, d[v] = {self.d[v]}")
        # print(self.adj[u])
        v_idx_in_w = self.get_adj_idx(u, v)

        # If the old cost is worse than the new cost
        # print(f"{self.d[v]} > {self.d[u]} + {self.w[u][v_idx_in_w]} is {self.d[v] > self.d[u] + self.w[u][v_idx_in_w]}")
        if self.d[v] > self.d[u] + self.w[u][v_idx_in_w]:
            # print(f"UPDATE d[v]: {self.d[v]}")
            self.d[v] = self.d[u] + self.w[u][v_idx_in_w]
            self.p[v] = u # Set a new best-predecessor
        # print(f"Final d[v]: {self.d[v]}")
        return

    def get_adj_idx(self, u, v):
        """
        O(n) lookup in a linked list adj[u], at position adj[u][v_idx_in_w], where its value is `v`
        """
        for _v in range(0, len(self.adj[u])):
            # print(_v)
            if self.adj[u][_v] == v: # Found location
                return _v # set index to be used for self.w[u][v]
        raise Exception(f"Error: Could not locate v = {v}'s index in adj[{u}]")
        return -1 
    
    def init_V(self):
        """
        Returns a working list of Vertices if desired.
        """
        # Initialize
        V = [v for v in range(0, len(self.adj))]
        # Check for empty Vertices and mark as EMPTY:
        # This is important. In my current graph structure, there's no way to determine if a node is just isolated, or if it is not present at all.
        for v in V:
            if self.adj[v] == []: #i.e. there are NO listed vertices connected
                V[v] = EMPTY # Then this is an empty node. Mark with something.
        return V

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