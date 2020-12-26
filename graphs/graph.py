# Graph

# Support for directed, weighted edges
# Vertices stored in an adjacency matrix
# Edges stored in a list?

class Graph():
    def __init__(self, adj):
        self.adj = adj # Adjacency list
        self.d = [] # List of shortest-path distance estimates for each vertex `v` in `V`

    def print_graph(self):
        """
        Prints graph as adjacency list
        """
        print("Printing graph:")

        for u in range(0, len(self.adj)):
            print(f"adj[{u}]: {self.adj[u]} \nd[{u}]: {self.d[u]}", end="\n")
        return

    def vertex_exist(self, s):
        """
        Answers if vertex `s` exists in `V`
        """
        if s >= len(self.adj) or s < 0:
            print("Error: Invalid source vertex `s`")
            return False

        # If source vertex exists, and has edges to other vertices
        if self.adj[s] != None:
            return True

        return False

    def initialize_d(self):
        """
        Initialize distance estimates `d[u]` to +infinity for all `u`
        """
        self.d = [float("+inf") for u in self.adj]
        return

# Unused atm
class Vertex():
    def __init__(self, v, w):
        self.v = v # Vertex Key
        self.w = w # Weight

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
    
    # def difference(V, s):
    #     """
    #     Finds the difference of 2 lists `V` and `s where 
    #     # (`s` is really a single vertex assumed to be in list `V`)
    #     """
    #     return [v for v in V if v not in s]