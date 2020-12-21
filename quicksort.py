# quicksort.py
import random

def quicksort(A, l, r):
    """
    Sorts elements in Theta(nlogn) time.
    """
    if (l < r):
        pivot = partition(A, l, r)
        quicksort(A, l, pivot - 1) # [l, r) - r is non-inclusive
        quicksort(A, pivot + 1, r)
    return

def partition(A, l, r):
    """
    Partitions the array into separate subarrays.
    Partition [l, i] contains elements "less than pivot"
    Partition (i, j) contains elements "greater than pivot"
    Partition [j, r) contains elements whose position is undetermined
    Element `r` is the pivot initially
    When sorting is complete, the pivot is swapped to the index between partitions [l, i] and the previous (i, j) partition
    """
    x = A[r] # x is the pivot element's value
    i = l - 1 # "no items" are "less than pivot" initially

    # Find rightmost bound `j` to encapsulate all items "less than pivot `x`"
    for j in range(l, r): # [l, r - 1] inclusive
        if A[j] <= x:
            i += 1 # `i` is the rightmost index bound on items "less than pivot" (i < j)
            swap(A, i, j) # where `i` is "less than pivot", and `j` was "greater than pivot"
    swap(A, i + 1, r) # swap the lower element (old pivot) `r` to the "less than pivot" subarray, and swap in the new pivot `i + 1`
    return i + 1 # return new pivot

def rand_partition(A, l, r):
    """
    Swap random item to be used as pivot, to the rightmost index.
    """
    i = random.randint(l, r) # [low, high] Inclusive pseudo-random number generator
    swap(A, r, i) # swap random element to the rightmost index
    return partition(A, l, r)

def swap(A, i1, i2):
    """
    Swaps 2 items in array A.
    """
    temp = A[i1]
    A[i1] = A[i2]
    A[i2] = temp
    return

def print_array(A):
    """
    Prints heap in spaced format.
    """
    if len(A) < 0:
        print("Error: Array length too small.")
        return
    print("Print Array: ", end="")
    for i in range(0, len(A)):
        print(A[i], end=" ")
    print("\n")
    return