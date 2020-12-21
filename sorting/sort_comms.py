# sort_comms.py - common sorting resources

# Test Inputs
arr0 = [1, 1, 1, 0]
arr1 = [1, 4, 3, 9, 8, 6, 5, 7, 2, 10]
arr2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
arr3 = [100, -200, 300, 450, 453, 123, 3, 231, -9, 213, 43, -45, 54, 0]

# Diagnostic Functions
def print_array(A):
    """
    Prints array in spaced format.
    """
    if len(A) < 0:
        print("Error: Array length too small.")
        return
    print("Print Array: ", end="")
    for i in range(0, len(A)):
        print(A[i], end=" ")
    print("\n")
    return