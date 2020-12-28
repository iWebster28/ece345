import graph as gr
import graph_comms as gc
import math

WHITE = "WHITE" # Undiscovered
GREY =  "GREY" # Discovered, but not finished exploring
BLACK = "BLACK" # Finished (found everything reachable from this vertex)

def main():
    # Build graph
    adj = gc.adj_a # Adjacency list 
    s = 1 # Source vertex
    G = gr.Graph(adj)

    dfs(G, s) # Perform bfs on graph `G`
    G.print_graph() # Print the graph's adjacency list
    return

def dfs(G, s):
    """
    Depth-First Search! For directed/undirected, unweighted graphs.
    """
    V = G.init_V()
           
    G.colour = [None for v in range(0, len(G.adj))]
    G.dt = [0 for v in range(0, len(G.adj))] # Discovery Time for vertices
    G.ft = [0 for v in range(0, len(G.adj))] # Finish Time for vertices
    G.time = 0

    # Initialize all colours to WHITE (unvisited)
    for u in V:
        if u is not gr.EMPTY:
            G.colour[u] = WHITE

    # Look for a WHITE node to explore
    for u in V:
        if u is not gr.EMPTY:
            if G.colour[u] == WHITE:
                dfs_visit(G, u)    
    return

def dfs_visit(G, u):
    """
    "Visit" a node/vertex by changing the colour to GREY
    and recursively visiting its children until there are no nodes left to explore in adj.
    Change colour to BLACK when finished, and record the finish time
    """
    # Discovering `u`
    G.colour[u] = GREY
    G.time += 1
    G.dt[u] = G.time

    # Exploring children `v` of `u`
    for v in G.adj[u]:
        if G.colour[v] == WHITE:
            dfs_visit(G, v)

    # Finished discovering all children
    G.colour[u] = BLACK
    G.time += 1
    G.ft[u] = G.time

if __name__ == "__main__":
    main()