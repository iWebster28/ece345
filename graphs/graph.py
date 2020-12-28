# Graph

# Support for directed, weighted edges
# Vertices stored in an adjacency matrix

class Graph():
    def __init__(self, adj, w=[]):
        self.adj = adj # Adjacency list
        self.d = [] # List of shortest-path distance estimates for each vertex `v` in `V`
        self.p = [] # List of predecessors
        self.w = w # List of weights for edges
        # self.V = [v for v in range(0, len(G.adj))]

    def print_graph(self):
        """
        Prints graph as adjacency list
        """
        print("----Printing graph----")

        for u in range(0, len(self.adj)):
            print(f"adj[{u}]: {self.adj[u]} \nd[{u}]: {self.d[u]}", end="\n")
            if len(self.p) is not 0:
                print(f"p[{u}]: {self.p[u]}\n--------")
                
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


# Unused atm
class Vertex():
    def __init__(self, v, w):
        self.v = v # Vertex Key
        self.w = w # Weight
        self.d = float("+inf") # Distance Estimate
        self.p = -1 # Predecessor vertex key

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