import graph as gr
import graph_comms as gc
import math

def main():
    # Build graph 
    V = gc.V
    E = gc.E
    s = 1 # source vertex
    G = gr.Graph(V, E)

    bfs(G, s) # Perform bfs on graph `G`

    G.print_graph() # Print the graph's adjacency list
    return

def bfs(G, s):
    """
    Breadth-First Search! For directed, unweighted graphs.
    """
    # Ensure s is a subset of G.V
    if not G.vertex_exist(s):
        print("Error: Invalid source vertex `s`")
        return    

    # Initialize distance estimates `ds`
    # (Could be moved to graph.py)
    # for u in G.difference(G.V, s):
    G.V.remove(s)
    G.initialize_d()
    
    G.d[s] = 0 # Source dist is initially 0
    Q = graph.Queue() # Create a queue
    Q.enqueue(s) # Add source vertex to the queue

    while len(Q.q) != 0: # While queue not empty
        u = Q.dequeue()
        # Visit all neighbours of vertex `v` (if unvisited),
        # Add 1 to distance estimate,
        # Then add v's neighbours to the Queue
        for v in G.adj[u]: 
            if G.d[v] == float("+inf"): # If vertex `v` is undiscovered:
                G.d[v] = G.d[u] + 1 # Increase distance estimate
                Q.enqueue(v) # Add neighbour to queue
    return

if __name == "__main__":
    main()
