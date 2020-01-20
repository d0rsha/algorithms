#!/usr/bin/env python
from unittest import TestCase
import subprocess
TESTNBR = 0


def testUnit(x, y, z):
    global TESTNBR
    TESTNBR += 1
    d = {'x': x, 'y': y, 'z': z}
    # solution

    # Command with shell expansion
    subprocess.call('echo ' + str(x) + " " + str(y) + " " +
                    str(z) + " > sample.in", shell=True)

    # ./addition-and-subtraction < sample.in > out
    subprocess.call(
        './addition-and-subtraction < sample.in > out1', shell=True)
    # trivial
    subprocess.call(
        'python3 addition-and-subtraction.py < sample.in > out2', shell=True)
    subprocess.call(
        'diff out out2 > /dev/null', shell=True)
    # Check ans
    res = subprocess.Popen('diff out out1', shell=True, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)

    res.wait()
    if res.wait() == 0:
        return res.returncode
    elif res.returncode == 1:
        print(' - ERROR - on test ', TESTNBR, ': ', d)
    else:
        print(' - ERROR - on test ', TESTNBR, '<CMD ERROR>: ',
              res.returncode, res, res.stdout)

    return res.returncode


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
