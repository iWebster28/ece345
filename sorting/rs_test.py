import radix_sort as rs
import sort_comms as sc

def main():
    A = sc.arr_pos_trip
    sc.print_array(A, "Input")
    B = rs.radix_sort(A, 3) # 3 digits/buckets
    sc.print_array(B, "Output")
    return

if __name__ == "__main__":
    main()