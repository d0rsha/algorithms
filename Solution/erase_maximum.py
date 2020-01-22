# -*- coding: utf-8 -*-
########################################
# Author: Anders Vrethem
# - Erasing Maxium
# [Input ] The first line contains an integer n (2 ≤ n ≤ 100), the length of the array. The second line contains integers A[1], A[2], . . . , A[n] (1 ≤ A[i] ≤ 100, 1 ≤ i ≤ n).
# [Output] Output n − 1 integers separated by spaces.
#
# [SOLUTION]
# Time Complexity: O(n)
# Description: Iterate trhough whole array once, keeping maxValue and maxIndex in memory

import sys

# import psutil


def main():
    n = input()
    a = list(map(int, input().split()))

    max = 0
    idx = -1
    counter = 0

    for i, val in enumerate(a):
        if max <= a[i]:
            if max == a[i]:
                counter = counter + 1
            else:
                counter = 1
                
            max = a[i]
            idx = i

    
    if counter > 3:
        for i in range(len(a) -1, -1, -1):
            if val == max:
                counter = counter -1
            pass
            
            if counter == 3:
                break
    else:
        pass

    result = a 
    result.pop(idx)
    result.sort()
    # print('Drop: a[', idx, '] = ', result.pop(idx))
    print(" ".join(map(str, result)))
    # print(psutil.virtual_memory())


if __name__ == '__main__':
    main()
