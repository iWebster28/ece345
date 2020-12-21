import quicksort as qs

def main():
    # A = [1, 4, 3, 9, 8, 6, 5, 7, 2, 10]
    A = [100, -200, 300, 450, 453, 123, 3, 231, -9, 213, 43, -45, 54, 0]
    qs.quicksort(A, 0, len(A) - 1)
    qs.print_array(A)
    return

if __name__ == "__main__":
    main()