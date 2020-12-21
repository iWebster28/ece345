import sort_comms as sc
def counting_sort(A, k=0):
    """
    Counting sort will stable-sort an array `A` in Theta(n + k) time.
    Input: Array A and input range (max value) `k`
    Output: Array B
    Range of A, B: [0, n)
    Range of C: [0, k]
    """
    n = len(A)
    B = [0 for i in range(0, n)]
    
    # [0, k] = range of your input, i.e. k is the largest number you'll see
    # We could manually determine k in O(n) time, or it could be pre-specified
    if (k == 0):
        # Find `k` manually
        for i in range(0, n):
            if A[i] > k:
                k = A[i]
    
    print(f"k: {k}")
    C = [0 for i in range(0, k + 1)] # Initialize all entries to 0 ("We've seen no instances of any number")
    # sc.print_array(C)
    
    # 1. How many #s exist from each value in original array A?
    for j in range(0, len(A)): # O(n)
        # print(f"{j}")
        # print(f"A[j] {A[j]}")
        C[A[j]] += 1 # Count how many times we've seen an instance of number `j` - store at index `A[j]` in array C
    # sc.print_array(C)

    # where C[A[j]] is "how many times" we've seen A[j] in array A

    # 2. "Prefix Sums" - count how many #s <= to that particular #
    for i in range(1, k + 1): # O(k)
        C[i] += C[i - 1] # Add previous value
    # sc.print_array(C)

    # 3. Place #s in appropriate position (sorts)
    # Range: [len(A), 1]
    for j in range(len(A) - 1, -1, -1): # O(n)
        # print(f"{j}")
        # print(f"C[A[j]] {C[A[j]]}")
        B[C[A[j]] - 1] = A[j] # Place value to final B array at index C[A[j]]
        C[A[j]] -= 1 # Indicate that we've "recorded" this value once in the final B array

    return B