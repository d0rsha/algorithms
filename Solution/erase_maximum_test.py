#!/usr/bin/env python3
import random
import re
import subprocess
from unittest import TestCase

OK = 0
NOK = 1
TESTNBR = 0


def write_sample_file(oneliner):
    """Write input to smaple.in"""
    with open("sample.in", 'w') as f:
        f.write(oneliner)
        f.write('\n')
        f.close()


def execute(argument):
    """Execute a shell command"""
    with open("sample.in", "r") as f:    
        proc = subprocess.Popen(argument, shell=True, stdin=f, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
    proc.wait()
    return get_output(proc)
 

def get_output(proc):
    """Get trimmed process output"""
    output = ''
    for line in iter(proc.stdout.readline, ''):
        if not line:
            break
        output += line.rstrip().decode('utf-8')

    proc.stdout.close() # Stream manually closed here 
    return output


def testUnit(x, l):
    """
    Test with given parameters
    # ToDo: Make multiprocess task?
    """

    global TESTNBR
    TESTNBR += 1
    dictionary = {'x': x, 'list': l}
    if not __debug__:
        print(f'Test{TESTNBR}: {dictionary}')

    l_string = re.sub("[\[|,|\]]", '', str(l))
    INPUT = f'{x} \n{l_string}'
    write_sample_file(INPUT)
    subject = execute('python3 erase_maximum.py')
    trivial = execute('./a.out')

    if subject == trivial:
        return 0
    else:
        print('############### ERROR on test: ', TESTNBR, ' ###############')
        print('---- INPUT: ')
        print(INPUT)
        print("---- Subject OUTPUT: ")
        print(subject)
        print("---- Correct OUTPUT: ")
        print(trivial)

    return 1


class LurrencyTest(TestCase):
    def testExamples(self):
        print(">>> examples(self) running")
        self.assertTrue(testUnit(3, [1,3,2]) == OK)
        self.assertTrue(testUnit(7, [4,1,4,2,4,3,4]) == OK)

    def testCornerCases(self):
        print(">>> cornerCases(self) running")
        # Corner tests
        #self.assertEqual(testUnit(2, [1, 100]), 0)
        #self.assertEqual(testUnit(2, [100, 100]), 0)
        self.assertEqual(testUnit(2, [1, 1]), 0)

    # Random tests
    def testRandomCases(self):
        print(">>> randomCases(self) running")
        lower, upper = 2, 100
        for i in range(lower, upper, int((upper - lower) / 98)):
            n = i
            l = []
            while ((n := n-1) >= 0):
                l.append(random.randint(lower, upper))

            self.assertEqual(testUnit(i, l), 0)

    def testNonWorking(self):
        print(">>> nonWorking(self) running")
        self.assertFalse(testUnit(38, [93, 65, 45, 15, 58, 80, 38, 26, 26, 93, 57, 9, 46, 48, 36, 37, 52, 49, 82, 45, 3, 34, 62, 24, 21, 22, 89, 17, 63, 21, 93, 16, 7, 9, 78, 91, 69, 100]))

if __name__ == '__main__':
    # test = LurrencyTest()
    # test.testCornerCases() 
    # test.testRandomCases()

    unittest.main()

# use : python3 -m unittest erase_maximum_test.py 
# -O  : explicit test info 
