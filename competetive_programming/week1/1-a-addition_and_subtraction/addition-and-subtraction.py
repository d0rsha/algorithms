# -*- coding: utf-8 -*-

import sys


def brute_force(x, y, z):
    i = 1
    a_even = 0

    if x - y == 0:
        return 1 if x == z else -1

    while (True):
        a_odd = a_even + x
        a_even = a_odd - y

        if a_odd == z:
            return 2*i - 1
        elif a_even == z:
            return 2*i

        if (a_odd > z and a_even > z) or (a_odd < 0 and a_even < 0):
            break
        # print("i", 2*i - 1, ":", a_odd, " i", 2*i, ":", a_even)
        i += 1
    return -1


def main():
    x, y, z = map(int, input().split())
    result = -1

    # your code
    result = brute_force(x, y, z)
    print(result)


if __name__ == '__main__':
    main()
