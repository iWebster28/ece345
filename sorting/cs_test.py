import counting_sort as cs
import sort_comms as sc

def main():
    A = sc.arr1
    sc.print_array(A)
    B = cs.counting_sort(A)
    sc.print_array(B)
    return

if __name__ == "__main__":
    main()