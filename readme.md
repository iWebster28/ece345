## What is this?
A little exploration into the depths of Algorithms and Data Structures. Based on the CLRS text.

## Projects

### Heapsort
* Run [heapsort_test.py](./sorting/heapsort_test.py) to see it in action.

#### Heapsort Characteristics:
* Comparison-based, in-place sorting algorithm 
* Time: O(nlogn)
* Space: O(1)

#### Heap Properties:
1. Heap shape property: bottom level of tree is not complete
2. Heap ordering: key(parent) > key(child)

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