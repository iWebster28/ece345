## What is this?
A little exploration into the depths of Algorithms and Data Structures. Based on the CLRS text.

## Projects

### Heapsort
* Run heapsort_test.py to see it in action.

#### Heapsort Characteristics:
* In-place sorting algorithm 
* Time complexity is O(nlogn)
* Space complexity is O(1)

#### Heap Properties:
1. Heap shape property: bottom level of tree is not complete
2. Heap ordering: key(parent) > key(child)

#### Node Indicies in a Heap:
* Root node begins at index 1, where 1 is the associated index in the array.

#### For any given node `i` in the heap/array:
1. Parent(i): math.floor(i/2)  
2. Left Child(i): 2*i   
3. Right Child(i): 2*i + 1  