# Heapsort Algorithm Review - Fall 2020 - Ian Webster
import math

class Heap:
    def __init__(self, input_array):
        if (len(input_array) < 1):
            print("Invalid input array size.")
        self.A = input_array
        
        self.start_idx = 1
        self.cvt_one_idx(input_array) # Convert to 1-indexed array
        # self.A.append(input_array[0]) # O(1) - Append 1st item to end of list (we ignore index 0)
        
        self.length = len(self.A) - 1
        self.heap_size = len(self.A) - 1 # Initially
        print('length:', self.length)
        print('heap_size:', self.heap_size)
    
    def cvt_one_idx(self, input_array):
        """
        Convert to 1-indexed array (shift all elements right)
        """
        self.start_idx = 1
        self.A.insert(1, input_array[0]) # O(n)
        return
    
    def cvt_zero_idx(self):
        """
        Convert to 0-indexed array (shift all elements left)
        """
        self.start_idx = 0
        self.A[:] = self.A[1:] # A[0] gets removed; all other elements shifted left
        self.length -= 1
        return

    # Return index corresponding to parent of node `i`
    def parent(self, i):
        return math.floor(i/2) 

    # Return index corresponding to right of node `i`
    def left(self, i): 
        return 2*i

    # Return index corresponding to left of node `i`
    def right(self, i):
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
        return

    def min_heapify(self, i):
        """
        min_heapify compares a node `i` with its children, and swaps the smaller child with `i`.
        Maintains the 'Heap Shape' property.
        Time: O(logn)

        This version of heapify is from CLRS.
        """ 
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and self.A[l] < self.A[i]:
            smallest = l
        else:
            smallest = i
        if r <= self.heap_size and self.A[r] < self.A[smallest]: # If `l` == `r`, then `r` is swapped with `i`
            smallest = r
        if smallest is not i:
            self.swap(i, smallest)
            self.min_heapify(smallest)
        return

    def build_heap(self, hs_type):
        """
        Builds a max heap, given array A.
        Starts from middle of array and 'heapifies' iteratively.
        Time: O(nlogn) (n calls to heapify)
        """
        print(f"---Building {hs_type} heap---")

        i = math.floor(len(self.A)/2) # Middle of the array; index `i` 
        while i != 0:
            if hs_type == "max":
                self.max_heapify(i)
            else:
                self.min_heapify(i)
            i = i - 1
        
        print("Heap built.")
        self.print_heap()
        return

    def extract_root(self, hs_type): # "similar to heap_extract_max"
        """
        Deletes/Extracts the max OR min node in a heap.
        """
        if (self.heap_size < 1):
            print("Error: heap_size too small.")
        
        root = self.A[1]
        self.swap(1, self.heap_size)
        self.heap_size = self.heap_size - 1
        if hs_type == "max":
            self.max_heapify(1)
        else:
            self.min_heapify(1)
        return root

    def heapsort(self, hs_type="max"):
        """
        Sorts array A in O(nlogn) time.
        """
        self.build_heap(hs_type)

        print("---Begin Sorting---")

        for i in range(1, self.heap_size):
            unused = self.extract_root(hs_type)
            # print("DIAG:", end=" ")
            # self.print_heap()

        # Shift back to 0-indexed array
        # self.cvt_zero_idx() 

        return
    
    def print_heap(self):
        """
        Prints heap in spaced format.
        """
        if self.length < 0 or self.heap_size < 0:
            print("Error: Heap length too small.")
            return
        print("Print heap: ", end="")
        for i in range(self.start_idx, self.length + 1):
            print(self.A[i], end=" ")
        print("\n")
        return

    def print_formatted(self):
        """
        Prints the array as a heap with appropriate spacing.
        Note: works for 1-indexed array.
        """
        n = self.length # number of nodes
        h = math.floor(math.log(n, 2)) # "height" of heap
        spacer = " "
        print(f"h: {h}")
        
        # For each row in the heap:
        for i in range(0, h + 1): # where `i` is row #; start at 0.
            # Start and End (min and max) node indices for row `i`
            start = 2 ** i
            if i == h: # Last row may not be full (b/c heap shape property)
                end = self.length
            else:
                end = 2 ** (i + 1) - 1
            
            expansion_factor = 3 # Adjust spacing of nodes
            delta_spacing = expansion_factor * (2 ** (h - i + 1)) - 1 # Determine spacing for consecutive elements `j` on row `i`
            init_spacing = expansion_factor * (2 ** (h - i) - 1) #delta_spacing - 1

            # print(f"delta: {delta_spacing}")
            # print(f"init: {init_spacing}")

            # Experimental: add logic to adjust spacing based on digit length of A[j]
            # Ex: Each row should consider the length (in digits) of its children
            # Easiest: consider the length of the longest number in the entire list (extract_max)
            # Use this number as the expansion factor, and then also subtract it from the delta on each consecutive hop?
            # num_digits = int(math.log10(self.A[self.length])) + 1 #self.A[2 ** (i + 2) - 1])
            # delta_spacing -= num_digits - 1

            if i == 0: # Corner case: first row
                print(spacer * init_spacing + f"{self.A[0]}", end="\n")
                continue
        
            # For each node `j` in row `i`
            for j in range(start, end + 1): # Indices of nodes in row `i` has range [2^i, 2^(i + 1) - 1]
                # The first node in any row begins with 2^(h - i) - 1 spaces.
                # Consecutive nodes require additional 2^(h - i + 1) - 1 spaces.

                # print(f"HI|{j}|{self.A[j]}|")
                if j == start:
                    print(spacer * init_spacing + f"{self.A[j]}", end="")
                else:
                    print(spacer * delta_spacing + f"{self.A[j]}", end="")
            
            print("") # Newline after ever row `i` is finished printing all nodes
        print("")
        return