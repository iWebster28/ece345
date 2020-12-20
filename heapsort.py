# Heapsort Algorithm Review - Fall 2020 - Ian Webster

# Heapsort Characteristics:
# In-place sorting algorithm (Space complexity is O(n))

# Heap Properties:
# 1. Heap shape property: bottom level of tree is not complete
# 2. Heap ordering: key(parent) > key(child)

# Node Indicies in a Heap:
# Root node begins at index 1, where 1 is the associated index in the array.

# For any given node `i` in the heap/array:
# 1. Parent(i): math.floor(i/2)
# 2. Left Child(i): 2*i 
# 3. Right Child(i): 2*i + 1

import math

class Heap:
    def __init__(self, input_array):
        if (len(input_array) < 1):
            print("Invalid input array size.")
        self.A = input_array
        self.A.append(input_array[0]) # Append 1st item to end of list (we ignore index 0)
        self.length = len(self.A) - 1
        self.heap_size = len(self.A) - 1 # Initially
        print('length:', self.length)
        print('hs:', self.heap_size)

    # Return index corresponding to parent of node `i`
    def parent(i):
        return math.floor(i/2) 

    # Return index corresponding to right of node `i`
    def left(i): 
        return 2*i

    # Return index corresponding to left of node `i`
    def right(i):
        return 2*i + 1

    def swap(self, i1, i2):
        """
        Swaps 2 nodes in array A; indices i1 and i2.
        """
        # print("swapping", i1, "and", i2)
        temp = self.A[i1]
        self.A[i1] = self.A[i2]
        self.A[i2] = temp
        return

    def max_heapify(self, i): # aka "extract max" or "bubble down"
        """
        max_heapify compares a node `i` with its children, and swaps the larger child with `i`.
        Maintains the 'Heap Shape' property.
        Time: O(logn)
        """    

        # print("max_heapify:", i, end="\n")

        try:
            if (2*i + 1 <= self.heap_size): # i.e. 2 children
                if (self.A[2*i] > self.A[i]) and (self.A[2*i] >= self.A[2*i + 1]): 
                    # Since 2*i is largest, swap left (2*i) with i 
                    self.swap(2*i, i)
                    self.max_heapify(2*i)
                    
                elif (self.A[2*i + 1] > self.A[i]) and (self.A[2*i + 1] > self.A[2*i]): 
                    # Since 2*i + 1 is largest, swap right (2*i + 1) with i
                    self.swap(2*i + 1, i)
                    self.max_heapify(2*i + 1)

            elif (2*i <= self.heap_size): # 1 child
                if (self.A[2*i] > self.A[i]):
                    self.swap(2*i, i)
                    self.max_heapify(2*i)
        except:
            print("Error: i=", i)

        return

    def build_max_heap(self):
        """
        Builds a max heap, given array A.
        Starts from middle of array and 'heapifies' iteratively.
        Time: O(nlogn) (n calls to heapify)
        """
        print("---Building Max Heap---")

        i = math.floor(len(self.A)/2) # Middle of the array; index `i` 
        while i != 0:
            self.max_heapify(i)
            i = i - 1
        
        print("Heap built.")
        self.print_heap()
        return

    def delete_max(self): # "similar to heap_extract_max"
        """
        Deletes the max node in a heap.
        """
        if (self.heap_size < 1):
            print("Error: heap_size too small.")
            
        self.swap(1, self.heap_size)
        self.heap_size = self.heap_size - 1
        self.max_heapify(1)
        return

    def heapsort(self):
        """
        Sorts array A in O(nlogn) time.
        """
        self.build_max_heap()

        print("---Begin Sorting---")

        for i in range(1, self.heap_size):
            self.delete_max()
            # print("DIAG:", end=" ")
            # self.print_heap()
        return
    
    def print_heap(self):
        if self.length < 0 or self.heap_size < 0:
            print("Error: Heap length too small.")
            return
        print("Print heap: ", end="")
        for i in range(1, self.length + 1):
            print(self.A[i], end=" ")
        print("\n")
        return