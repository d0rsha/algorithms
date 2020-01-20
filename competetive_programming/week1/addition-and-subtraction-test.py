#!/usr/bin/env python
from unittest import TestCase
import subprocess
TESTNBR = 0


def write_input():
    """Write input to smaple.in"""
    pass


def execute(argument):
    """Execute a shell command"""
    proc = subprocess.Popen(argument, shell=True, stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
    proc.wait()
    return proc


def get_output(proc):
    output = ''
    for line in iter(proc.stdout.readline, ''):
        if not line:
            break
        output += line.rstrip().decode('utf-8')
    return output


def testUnit(x, y, z):
    global TESTNBR
    TESTNBR += 1
    d = {'x': x, 'y': y, 'z': z}

    execute(f'echo {x} {y} {z} > sample.in')
    subject = execute('./addition-and-subtraction < sample.in')
    trivial = execute('python3 addition-and-subtraction.py < sample.in')

    subject_out = get_output(subject)
    trivial_out = get_output(trivial)

    if subject_out == trivial_out:
        return 0
    else:
        print('############### ERROR on test: ', TESTNBR, ' ###############')
        print('---- INPUT: ', d)
        print("---- Subject OUTPUT: ")
        print(subject_out)
        print("---- Correct OUTPUT: ")
        print(trivial_out)

    return 1


class LurrencyTest(TestCase):
    def testMultiplication(self):
        # Corner tests
        testUnit(1, 1, 1)
        testUnit(1, 1000, 1)
        testUnit(1, 1, 1000)
        testUnit(1000, 1000, 1)
        testUnit(1000, 1000, 1000)
        # self.assertEqual(testUnit(1, 1, 1), 0)

    # Random tests
    # until[$X - gt 1000]
    # do
    # Y = 1
    # Z = 1
    # # Loop Y
    # until[$Y - gt 1000]
    # do
    # # Loop X
    # Z = 1
    #  until[$Z - gt 1000]
    #   do
    #    # Loop Z
    #    echo "Test [$i] X=$X Y=$Y Z=$Z \t\t - OK"
    #      echo "$X $Y $Z \n" > sample.in

    #       # solution
    #       ./addition-and-subtraction < sample.in > out
    #        # trivial
    #        python3 addition-and-subtraction.py < sample.in > out_trivial
    #         # Check ans
    #         diff out out_trivial > /dev/null

    #         if [$? -ne '0']
    #          then
    #           echo "Error on test"
    #            return 13
    #             fi

    #             Z =$((Z+65))
    #             i =$((i+1))
    #         done
    #         Y =$((Y+65))
    #     done

    #     X =$((X+65))
    # done
    # echo " -- ALL $i TEST OK -- "


if __name__ == '__main__':
    x = LurrencyTest()
    x.testMultiplication()
    # unittest.main()
