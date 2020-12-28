## What is this?
A little exploration into the depths of Algorithms and Data Structures to enhance my understanding. Based on the CLRS text.

## Sorting Algorithms

### Heapsort
* Run [heapsort_test.py](./sorting/heapsort_test.py) to see it in action.

#### Heapsort Characteristics:
* Comparison-based, in-place sorting algorithm 
* Time: O(nlogn)
* Space: O(1)

#### Heap Properties:
1. Heap shape property: bottom level of tree is not complete
2. Heap ordering
* Max-Heap Property: key(parent) >= key(child)
* Min-Heap Property: key(parent) <= key(child)

#### Node Indicies in a Heap:
* Root node begins at index 1, where 1 is the associated index in the array.

#### For any given node `i` in the heap/array:
1. Parent(i): math.floor(i/2)  
2. Left Child(i): 2*i   
3. Right Child(i): 2*i + 1  


### Quicksort
* Run [qs_test.py](./sorting/qs_test.py) to see it in action

#### Quicksort Characteristics:
* Comparison-based sorting algorithm
* Time: Theta(nlogn) on average
* Space: O(n)
* Randomized partition used to prevent the ```T(n) = T(n - 1) + Theta(n) = Theta(n^2)``` worst case
* Partitions explained further in [quicksort.py](./sorting/quicksort.py)


### Counting Sort
* Run [cs_test.py](./sorting/cs_test.py) to see it in action

#### Counting Sort Characteristics:
* Stable sorting algorithm
* Must have **positive** input integers in range [0, k] only
* Time: Theta(n + k), where k is max value of input array

### Radix Sort
* Run [rs_test.py](./sorting/rs_test.py) to see it in action
* Stable sorting algorithm
* Key idea: sort from LSB (least significant bit) to MSB (most " ") (or digit)
``` 
    n = # of numbers in array A
    b = b-bit numbers, if binary (ex: 32-bit)
    r = bucket size in bits (ex: 8-bit buckets)
    k = range of values per bucket/digit (i.e. max #)
    where k = 2^r (r = 3 yields 8 bits/bucket)
    d = # 'digits' for each number
    where d = b/r = # passes/bucket or passes/digit
```
**Time EX1:** n = 100, b = 32, r = 8, k = 2^r = 2^3 = 8  
Theta(# buckets * time per bucket)  
= Theta(d(n + k))   
= Theta((b/r)(n + 2^r))  
= Theta((32/8)(100 + 2^8)) = Theta(4(100 + 2^8))  

**Time EX2:** (see arr_pos_trip in [sort_comms.py](./sorting/sort_comms.py)) n = 7, k = 10 (10 decimal numbers per 1 digit), d = 3 passes (max number in array A has 3 digits)  
Theta(# buckets * time per bucket)  
= Theta(d(n + k))  
= Theta(3(7 + 10))  


## Graph Algorithms
* For graphs G = (V, E)
* V = Vertices, E = Edges
* Graphs represented by **adjacency list** where:
* V = {u | u in [0, len(G.adj))}
* E = {(u, v) | u in [0, len(G.adj) and v in G.adj[u]}
* See [graph.py](./graphs/graph.py) for more details on graph structure.
* Weights, Predecessors, Distance Estimates, and Adjacency lists are stored separately. V and E may be interpreted from the Adjacency list. 

### Breadth-First Search (BFS)
* Run [bfs.py](./graphs/bfs.py) to see it in action
* For directed or undirected, unweighted graphs.
* Finds the shortest paths from source vertex `s` to every other vertex
* Uses a **queue** to maintain a "wavefront" of encountered vertices
* The "neighbours" of each encountered vertex is explored
* The predecessor vertex for each vertex is stored in the `p` array
* Paths can be printed by printing predecessors recursively (not implemented)
* Time: O(V + E)
* Note: BFS may not reach all vertices.

### Bellman-Ford (Single-Source Shortest Paths)
* Run [bellman_ford.py](./graphs/bellman-ford.py) to see it in action
* Supports negative-weight edges, unlike Dijkstra.
* Returns true when no negative weight cycles are reachable from source vertex `s`. Returns false otherwise.
* Every edge is "relaxed" >= 1 time
* Time: O(VE)

### Dijkstra's Algorithm (Single-Source Shortest Paths)
* Maintains a set of 2 vertices:
* S = vertice sfor which true shortest path weight has been determined
* pq = priority queue = `V` - `s`
* Time: O(ElogV)
* Note: Cannot use with graphs containing negative-weight edges