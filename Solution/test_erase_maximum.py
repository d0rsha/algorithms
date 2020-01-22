# -*- coding: utf-8 -*-
########################################
# Author: Anders Vrethem
# - Test cases for algorithms
# - Erasing Maxium
# [Input ] The first line contains an integer n (2 ≤ n ≤ 100), the length of the array. The second line contains integers A[1], A[2], . . . , A[n] (1 ≤ A[i] ≤ 100, 1 ≤ i ≤ n).
# [Output] Output n − 1 integers separated by spaces.

import os
import random
import re
import subprocess
import sys
from subprocess import call

# import psutil


def main():
    print('Begin Test of erasing_maximum')

    for n in range(2, 4, 2):
        random_list = [random.randint(1, 100) for i in range(n)]
        print('Random list: ', random_list)
        process = subprocess.Popen(['python3', 'Solution/erase_maximum.py'],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        input, output = process.stdin, process.stdout
x
        print(bytes(str(n), 'utf-8').decode('utf-8'))
        print(bytes(re.sub('[\[|\,|\]]', '',
                           str(random_list)), 'utf-8').decode('utf-8'))

        input.write(bytes(str(n), 'utf-8'))
        input.write(bytes(re.sub('[\[|\,|\]]', '', str(random_list)), 'utf-8'))

        print(input.read())
        stdoutdata, stderrdata = process.communicate(
            input=input.decode('utf-8'))
        # stdoutdata, stderrdata = process.communicate(bytes("%s \n" % re.sub(
        #     '[\[|\,|\]]', '', str(random_list)), 'utf-8'))

        # print(output.read().decode('utf-8'))

        # input.close()
        # output.close()
        # status = process.wait()
        # print('Status = ', status)

        # inputdata = bytes(str(n) + " \n" + str(random_list), 'utf-8')
        # stdoutdata, stderrdata = process.communicate("%d \n" % n)

        print(stdoutdata)

        print(stderrdata)
        # call(['python3', 'Solution/erase_maximum.py'])
        # os.system("echo %d" % n)
        # os.system("echo %s" % random_list)


if __name__ == '__main__':
    main()





re.sub('[\[|\,|\]]', '', str(random_list))
