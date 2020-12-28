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

    bellman_ford(G, s)
    G.print_graph()
    return

def bellman_ford(G, s):
    """
    Bellman Ford Algorithm - find shortest paths from source vertex `s` to all other nodes.
    Time: O(VE)
    """
    G.init_ss(s)

    for i in range(0, len(G.adj)): # [0, len(G.adj))
        for u in range(0, len(G.adj)): # for (u, v) in G.E:
            for v in G.adj[u]:
                G.relax(u, v)

    for u in range(0, len(G.adj)): # for (u, v) in G.E:
        for v in G.adj[u]:
            if G.d[v] > G.d[u] + G.w[u][G.get_adj_idx(u, v)]:
                return False
    return True

if __name__ == "__main__":
    main()