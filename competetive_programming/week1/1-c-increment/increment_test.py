#!/usr/bin/env python3
import random
import re
import subprocess
from unittest import TestCase

OK = 0
NOK = 1
TESTNBR = 0


def SET_INPUT(oneliner):
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

    proc.stdout.close()  # Stream manually closed here
    return output


def runTest(x):
    """
    Return result from script
    """
    SET_INPUT(f'{x}')
    global FILE
    return execute(f'python3 {FILE}')


# test must start with 'test' for unittest to identify test case
class UnitTest(TestCase):
    def testSmallTest(self):
        print(">>>> Small")
        self.assertEqual(runTest(9999), '5')
        self.assertEqual(runTest(9990), '4')
        self.assertEqual(runTest(8999), '4')
        self.assertEqual(runTest(9989), '4')

    def testNonWorking(self):
        print(">>>> Big ")
        self.assertEqual(runTest(9999999999), '11')
        self.assertEqual(runTest(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999), '101')
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)

FILE = 'increment.py'
# use : python3 -m unittest erase_maximum_test.py
# -O  : explicit test info
