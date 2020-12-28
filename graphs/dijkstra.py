import graph_comms as gc
import graph as gr
import copy
import sys
sys.path.insert(1, "../sorting/")

import heapsort as hs
import sort_comms as sc

def main():
    # Get source vertex `s` from argument 1
    if len(sys.argv) != 2:
        s = 4
    else:
        s = int(sys.argv[1])
    adj = gc.adj_c
    w = gc.weight_c
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

    V = [v for v in range(0, len(G.adj))] # Add all vertices to queue initially

    # Heap uses distance estimates of vertices sa the key for "extract_root"
    # values: vertices, keys: distance estimates
    pq = hs.PriorityQueue(V, copy.deepcopy(G.d)) # Priority Queue/Heap - keyed by `d` distance estimate
    pq.build_heap("min") # Applies only to the keys `G.d`
    # pq.print_heap() # 1-indexed
    # pq.print_heap_idx() # 1-indexed
    
    while pq.heap_size is not 0:
        min_d, u = pq.extract_root("min") # Min-heap Extract-Min with lowest distance estimate
        # print(f"u: {u}, min_d: {min_d}")
        # print(f"G.d[u]: {G.d[u]}")
        S.append(u)
        # print(f"---------{S}---------")
        for v in G.adj[u]:
            G.relax(u, v) # w array is contained with the Graph class

    return

if __name__ == "__main__":
    main()