# heapsort_test.py
import heapsort as hs
import sort_comms as sc

def main():
    # Call heapsort on array A
    input_array = sc.arr1
    heap = hs.Heap(input_array)
    heap.print_heap()
    heap.heapsort("max")
    print("Sorted List: ", end="")
    heap.print_heap()
    heap.print_formatted()
    return

if __name__ == "__main__":
    main()
    