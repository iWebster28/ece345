import sort_comms as sc
import counting_sort as cs

def radix_sort(A, d):
    """
    Perform radix sort on array `A`.
    n = # of numbers in array `A`
    k = range of digits (i.e. max #)
    d = # 'digits' for each number
    """
    # Stable sort on digit i in Array A
    for i in range(1, d + 1): 
        # print(f'{i}')
        A = modified_cs(A, i, d)
        # sc.print_array(A)
    return A

def modified_cs(A, x, d):
    """
    Perform counting sort on digit `x` of all numbers in array `A`
    Input: Array A 
    Output: Array B
    Range of A, B: [0, n)
    Range of C: [0, k]
    x = digit `x` to perform stable sort on.
    d = # passes or digits total of 1 number of array A
    """
    n = len(A)
    B = [0 for i in range(0, n)]

    # [0, k] = range of your input, i.e. k is the largest number you'll see
    k = 10 # for decimal digits!
    # Better: use value of `d` to calculate range per digit = k

    # print(f"k: {k}")
    C = [0 for i in range(0, k + 1)] # Initialize all entries to 0 ("We've seen no instances of any number")
    
    # 1. How many #s exist from each value in original array A?
    for j in range(0, len(A)): # O(n)
        C[sc.xth_digit(A[j], x)] += 1 # Count how many times we've seen an instance of number `j` - store at index `A[j]` in array C

    # where C[A[j]] is "how many times" we've seen A[j] in array A

    # 2. "Prefix Sums" - count how many #s <= to that particular #
    for i in range(1, k + 1): # O(k)
        C[i] += C[i - 1] # Add previous value

    # 3. Place #s in appropriate position (sorts)
    # Range: [len(A), 0]
    for j in range(len(A) - 1, -1, -1): # O(n)
        B[C[sc.xth_digit(A[j], x)] - 1] = A[j] # Place value to final B array at index C[A[j]]
        C[sc.xth_digit(A[j], x)] -= 1 # Indicate that we've "recorded" this value once in the final B array

    return B