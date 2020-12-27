# graph_comms.py

# Test Inputs
# V = [1, 2, 3, 4, 5, 6]
# E = [6, 7, 8, 9, 0]

# Test adjacency lists

# Fig 22.1 in CLRS (undirected, unweighted)
adj_a = [[] for i in range(0, 6)]
adj_a[1] = [2, 5]
adj_a[2] = [1, 5, 3, 4]
adj_a[3] = [2, 4]
adj_a[4] = [2, 5, 3]
adj_a[5] = [4, 1, 2]


# Fig 22.2 in CLRS (directed, unweighted)
adj_b = [[2, 4], [5], [6, 5], [2], [4], [6]]

# Directed, weighted
adj_c = [[2, 4], [5], [6, 5], [2], [4], [6]]
weight_c = [[20, 10], [50], [24, 31], [25], [41], [21]]