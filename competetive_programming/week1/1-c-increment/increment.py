# -*- coding: utf-8 -*-
########################################
# Author: Anders Vrethem
# - Increment 
# [Input ] A non-negative integer x (0 ≤ x ≤ 101 000 000) with no leading zeroes.
# [Output] The number of decimal digits in (x + 1).
#
# [SOLUTION]
# Time Complexity: O(n)
# Description: Iterate through number as a string, if char is 9: carry, else ++

import sys


def main():
    line = input()

    carry = True
    for i in range(len(line) -1, -1, -1):
        c = line[i]
        if int(c) == 9 and carry:
            carry = True
        else:
            carry = False
            break
        # print(i, c, carry)

    print(len(line) + int(carry))
    
if __name__ == '__main__':
    main()
