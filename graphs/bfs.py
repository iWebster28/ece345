import graph as gr
import graph_comms as gc
import math

def main():
    # Build graph
    adj = gc.adj_a # Adjacency list 
    s = 1 # Source vertex
    G = gr.Graph(adj)

    bfs(G, s) # Perform bfs on graph `G`
    G.print_graph() # Print the graph's adjacency list
    return

def bfs(G, s):
    """
    Breadth-First Search! For directed, unweighted graphs.
    """
    # Ensure s is a subset of G.V
    if not G.vertex_exist(s):
        return    

    # Initialize distance estimates `d`
    G.init_ss(s)
   
    Q = gr.Queue() # Create a queue
    Q.enqueue(s) # Add source vertex to the queue

    while len(Q.q) is not 0: # While queue not empty
        u = Q.dequeue()
        # Visit all neighbours of vertex `v` (if unvisited),
        # Add 1 to distance estimate,
        # Then add v's neighbours to the Queue
        for v in G.adj[u]:
            if G.d[v] == float("+inf"): # If vertex `v` is undiscovered:
                G.d[v] = G.d[u] + 1 # Increase distance estimate
                Q.enqueue(v) # Add neighbour to queue
    return

if __name__ == "__main__":
    main()