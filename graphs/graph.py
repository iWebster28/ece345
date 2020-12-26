# Graph

# Support for directed, weighted edges
# Vertices stored in an adjacency matrix
# Edges stored in a list?

class Graph():
    def __init__(self, V, E):
        self.V = []
        self.E = [] # list of tuples?
        self.adj = [] # Adjacency list - is this built from E?

        self.d = [] # List of shortest-path distance estimates for each vertex `v` in `V`

        self.build_adj_list()

    # Assume adj list is already build
    # def build_adj_list(self):
    #     """
    #     Builds an adjacency list using V and E.
    #     """
    #     for u in V:
    #         self.adj[u] = []

    #     return

    def print_graph(self):
        """
        Prints graph as adjacency list
        """
        print("Printing graph:")


        
        return

    def vertex_exist(self, s):
        """
        Answers if vertex `s` exists in `V`
        """
        for v in self.V:
            if v == s:
                return True
        return False

    def initialize_d(self):
        """
        Initialize distance estimates `d[u]` to +infinity for all `u`
        """
        for u in self.V:
            self.d[u] = float("+inf")
        return

class Vertex():
    def __init__(self, v, w):
        self.v = 

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
    
    def difference(V, s):
        """
        Finds the difference of 2 lists `V` and `s where 
        # (`s` is really a single vertex assumed to be in list `V`)
        """
        return [v for v in V if v not in s]