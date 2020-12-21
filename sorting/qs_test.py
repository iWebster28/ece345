import quicksort as qs
import sort_comms as sc

def main():
    A = sc.arr3
    sc.print_array(A, "Input")
    qs.quicksort(A, 0, len(A) - 1)
    sc.print_array(A, "Output")
    return

if __name__ == "__main__":
    main()