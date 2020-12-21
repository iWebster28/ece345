# sort_comms.py - common sorting resources

# Test Inputs
arr0 = [1, 1, 1, 0]
arr1 = [1, 4, 3, 9, 8, 6, 5, 7, 2, 10]
arr2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
arr3 = [100, -200, 300, 450, 453, 123, 3, 231, -9, 213, 43, -45, 54, 0]
arr_pos_trip = [857, 814, 724, 937, 152, 654, 112]

# Diagnostic Functions
def print_array(A, msg="Print Array"):
    """
    Prints array in spaced format.
    """
    if len(A) < 0:
        print("Error: Array length too small.")
        return
    print(f"{msg}: ", end="")
    for i in range(0, len(A)):
        print(A[i], end=" ")
    print("\n")
    return

def xth_digit(n, x):
    """
    Gets the xth digit of a number `n`
    """
    # k = 5 #want kth digit
    # n = 12345678

    for i in range(0, x - 1):
        n = int(n / 10)
    n %= 10

    # print(n)
    return n