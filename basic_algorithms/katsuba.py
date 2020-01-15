from math import ceil, floor


def karatsuba(x, y):
    n = max(len(str(x)), len(str(y)))
    # Cast n into a float because n might lie outside the representable range of integers.
    m = ceil(n/2)

    # base case
    if n == 1:  # in other words, if x and y are single digits
        return x * y

    a = floor(x / int(10**m))
    b = (x % int(10**m))

    c = floor(y / int(10**m))
    d = (y % int(10**m))

    p = a + b
    q = c + d

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    pq = karatsuba(p, q)

    adbc = pq - ac - bd

    return int(10**n)*ac + int(10**(n/2)) * adbc + bd


print(karatsuba(12, 12))
print(karatsuba(0, 0))
print(karatsuba(1234, 5678))
print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                2718281828459045235360287471352662497757247093699959574966967627))
