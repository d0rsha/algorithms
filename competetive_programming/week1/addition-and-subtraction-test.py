#!/usr/bin/env python
import random
import subprocess
from unittest import TestCase

TESTNBR = 0


def write_sample_file(oneliner):
    """Write input to smaple.in"""
    with open("sample.in", 'w') as f:
        f.write(oneliner)
        f.write('\n')
        f.close()


def execute(argument):
    """Execute a shell command"""
    proc = subprocess.Popen(argument, shell=True, stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
    proc.wait()
    return get_output(proc)


def get_output(proc):
    """Get trimmed process output"""
    output = ''
    for line in iter(proc.stdout.readline, ''):
        if not line:
            break
        output += line.rstrip().decode('utf-8')
    return output


def testUnit(x, y, z):
    """
    Test with given parameters
    # ToDo: Make multiprocess task?
    """

    global TESTNBR
    TESTNBR += 1
    dictionary = {'x': x, 'y': y, 'z': z}
    print(f'Test{TESTNBR}: {dictionary}')

    #execute(f'echo {x} {y} {z} > sample.in')
    write_sample_file(f'{x} {y} {z}')
    subject = execute('./addition-and-subtraction < sample.in')
    trivial = execute('python3 addition-and-subtraction.py < sample.in')

    if subject == trivial:
        return 0
    else:
        print('############### ERROR on test: ', TESTNBR, ' ###############')
        print('---- INPUT: ', dictionary)
        print("---- Subject OUTPUT: ")
        print(subject)
        print("---- Correct OUTPUT: ")
        print(trivial)

    return 1


class LurrencyTest(TestCase):
    def testCornerCases(self):
        # Corner tests
        self.assertEqual(testUnit(1, 1, 1), 0)
        self.assertEqual(testUnit(1, 1000, 1), 0)
        self.assertEqual(testUnit(1, 1, 1000), 0)
        self.assertEqual(testUnit(1000, 1000, 1), 0)
        self.assertEqual(testUnit(1000, 1000, 1000), 0)
        # self.assertEqual(testUnit(1, 1, 1), 0)

    # Random tests
    def testRandomCases(self):
        n, lower, upper = 2, 2, 1000
        for i in range(lower, upper, int((upper - lower) / 100)):
            x, y, z = random.randint(lower, i), random.randint(
                lower, i), random.randint(lower, i)
            self.assertEqual(testUnit(x, y, z), 0)


if __name__ == '__main__':
    # test = LurrencyTest()
    # test.cornerCases()
    # test.randomCases()

    unittest.main()
