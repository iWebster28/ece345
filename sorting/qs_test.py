import quicksort as qs
import sort_comms as sc

def main():
    A = sc.arr3
    qs.quicksort(A, 0, len(A) - 1)
    sc.print_array(A)
    return

if __name__ == "__main__":
    main()