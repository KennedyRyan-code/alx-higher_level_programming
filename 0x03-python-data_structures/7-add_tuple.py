#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # the first two elements of each tuple
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0

    # Perform the addition
    sum1 = a1 + b1
    sum2 = a2 + b2

    # Return the new tuple sum
    return (sum1, sum2)
