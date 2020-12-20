# heapsort_test.py
import heapsort as hs

def main():
    # Call heapsort on array A
    # input_array = [1, 4, 3, 9, 8, 6, 5, 7, 2, 10]
    input_array = [100, -200, 300, 450, 453, 123, 3, 231, -9, 213, 43, -45, 54, 0]
    
    heap = hs.Heap(input_array)
    heap.print_heap()
    heap.heapsort()
    print("Sorted List: ", end="")
    heap.print_heap()
    
    return


if __name__ == "__main__":
    main()
    