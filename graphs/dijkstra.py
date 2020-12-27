import graph_comms as gc
import graph as gr

import heapsort as hs
import sort_comms as sc

def main():
    adj = gc.adj_c
    s = 1 
    G = gr.Graph(adj)

    dijkstra(G, s)
    G.print_graph()
    return

def dijkstra(G, s):
    """
    Dijkstra's algorithm - find shortest paths from source vertex `s` to all other nodes.
    """
    G.init_ss(s)
    S = []

    # Call heapsort on array A
    input_array = sc.arr1
    heap = hs.Heap(input_array)
    heap.print_heap()
    heap.heapsort()
    print("Sorted List: ", end="")
    heap.print_heap()
    heap.print_formatted()

    pq = [] # Priority Queue

    # Q = gr.Queue() # Priority Queue using heap!
    pq = [v for v in G.adj] # Add all vertices to queue initially

    while len(pq) is not 0:
        u = pq.extract_min() # min heap!
        S.append(u)
        for v in G.adj[u]:
            G.relax(u, v, w)

    return

if __name__ == "__main__":
    main()