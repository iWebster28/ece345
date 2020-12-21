import radix_sort as rs
import sort_comms as sc

def main():
    A = sc.arr_pos_trip
    sc.print_array(A, "Input")

    # Passes
    # d = 3
    # Get d manually - if based on max # digits
    d = sc.get_d_digits(A)

    B = rs.radix_sort(A, d) # 3 digits/buckets
    sc.print_array(B, "Output")
    return

if __name__ == "__main__":
    main()