import graph_comms as gc
import graph as gr
import sys
sys.path.insert(1, "../sorting/")

import heapsort as hs
import sort_comms as sc

def main():
    adj = gc.adj_c
    w = gc.weight_c
    s = 4
    G = gr.Graph(adj, w)

    dijkstra(G, s)
    G.print_graph()
    return

def dijkstra(G, s):
    """
    Dijkstra's algorithm - find shortest paths from source vertex `s` to all other nodes.
    Time: O(VlogE)
    """
    G.init_ss(s)
    S = [] # Vertices whose final shortest path weight has been determined

    # Call heapsort on array A
    V = [v for v in range(0, len(G.adj))] # Add all vertices to queue initially

    # Heap uses distance estimates of vertices
    pq = hs.Heap(G.d) # Priority Queue/Heap
    pq.print_heap() # 1-indexed

    while pq.heap_size is not 0:
        u_idx = pq.extract_root("min") # Min-heap Extract-Min with lowest distance estimate
        u = V[u_idx]
        S.append(u)
        print(f"---------{S}---------")
        for v in G.adj[u]:
            G.relax(u, v) # w array is contained with the Graph class

    return

if __name__ == "__main__":
    main()