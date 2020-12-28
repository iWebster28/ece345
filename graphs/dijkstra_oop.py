import graph_comms as gc
import graph_oop as gr
import copy
import sys
sys.path.insert(1, "../sorting/")

import heapsort_oop as hs
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

    # In OOP version, 0th element of each list is the Vertex (not ListVertex)
    V = [G.new_adj[v][0] for v in range(0, len(G.new_adj))] # Add all vertices to queue initially
    print(V)

    # Heap uses distance estimates of vertices sa the key for "extract_root"
    # values: vertices, keys: distance estimates
    pq = hs.PriorityQueue(V) # Priority Queue/Heap - keyed by `d` distance estimate
    pq.build_heap("min") # Applies only to the keys `G.d`
    # pq.print_heap() # 1-indexed
    # pq.print_heap_idx() # 1-indexed
    
    while pq.heap_size is not 0:
        u = pq.extract_root("min") # Min-heap Extract-Min with lowest distance estimate
        # print(f"u: {u.u}, min_d: {u.d}")
        # print(f"G.d[u]: {G.d[u]}")
        S.append(u.u)
        # print(f"---------{S}---------")
        for v_idx in range(1, len(G.new_adj[u.u])): # Begin at 1 since our Vertex `u` is at idx 0 in the same list as ListVertices `v`
            # print(G.new_adj[u.u][v_idx])
            G.relax(u.u, G.new_adj[u.u][v_idx].v) # w array is contained with the Graph class

    return

if __name__ == "__main__":
    main()