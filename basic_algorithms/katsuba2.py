from math import ceil, floor

# math.ceil(x) Return the ceiling of x as a float, the smallest integer value greater than or equal to x.
# math.floor(x) Return the floor of x as a float, the largest integer value less than or equal to x.


def karatsuba_old(x, y):
    # base case
    if x < 10 and y < 10:  # in other words, if x and y are single digits
        return x*y

    n = max(len(str(x)), len(str(y)))
    # Cast n into a float because n might lie outside the representable range of integers.
    m = ceil(n/2)

    x_H = floor(x / 10**m)
    x_L = x % (10**m)

    y_H = floor(y / 10**m)
    y_L = y % (10**m)

    # recursive steps
    a = karatsuba_old(x_H, y_H)
    d = karatsuba_old(x_L, y_L)
    e = karatsuba_old(x_H + x_L, y_H + y_L) - a - d

    return int(a*(10**(m*2)) + e*(10**m) + d)


def karatsuba(x, y):
    """Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = n / 2

        a = x / 10**(nby2)
        b = x % 10**(nby2)
        c = y / 10**(nby2)
        d = y % 10**(nby2)

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a+b, c+d) - ac - bd

        # this little trick, writing n as 2*nby2 takes care of both even and odd n
        prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

        return prod


def zeroPad(numberString, zeros, left=True):
    """Return the string with zeros added to the left or right."""
    for i in range(zeros):
        if left:
            numberString = '0' + numberString
        else:
            numberString = numberString + '0'
    return numberString


def karatsubaMultiplication(x, y):
    """Multiply two integers using Karatsuba's algorithm."""
    # convert to strings for easy access to digits
    x = str(x)
    y = str(y)
    # base case for recursion
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    if len(x) < len(y):
        x = zeroPad(x, len(y) - len(x))
    elif len(y) < len(x):
        y = zeroPad(y, len(x) - len(y))
    n = len(x)
    j = n//2
    # for odd digit integers
    if (n % 2) != 0:
        j += 1
    BZeroPadding = n - j
    AZeroPadding = BZeroPadding * 2
    a = int(x[:j])
    b = int(x[j:])
    c = int(y[:j])
    d = int(y[j:])
    # recursively calculate
    ac = karatsubaMultiplication(a, c)
    bd = karatsubaMultiplication(b, d)
    k = karatsubaMultiplication(a + b, c + d)
    A = int(zeroPad(str(ac), AZeroPadding, False))
    B = int(zeroPad(str(k - ac - bd), BZeroPadding, False))
    return A + B + bd


print('Old: ', karatsuba_old(1234, 5678))
print('Old: ', karatsuba_old(12, 12))
print('Old: ', karatsuba_old(0, 0))
print('Old: ', karatsuba_old(1234, 4321))
print('Old: ', karatsuba_old(3141592653589793238462643383279502884197169399375105820974944592,
                             2718281828459045235360287471352662497757247093699959574966967627))

print(karatsubaMultiplication(12, 12))
print(karatsubaMultiplication(0, 0))
print(karatsubaMultiplication(1234, 4321))
print(karatsubaMultiplication(3141592653589793238462643383279502884197169399375105820974944592,
                              2718281828459045235360287471352662497757247093699959574966967627))


# 8539734222673566957498846900491595793628487889746454950813687461572372213054499114931277629325900131223124341791952806582723184
# 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
