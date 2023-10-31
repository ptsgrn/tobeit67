#! /usr/bin/env python3
import os
import sys
import time

argv = sys.argv

class colors:
    green = '\033[92m'
    red = '\033[91m'
    end = '\033[0m'

if len(argv) != 2:
    print("Usage: python testcase.py <testcase>")
    sys.exit(0)

problem = argv[1]

# get all file named like `41(1).tc` where 41 is the problem number
# and 1 is the testcase number

testcases = [f for f in os.listdir("problems") if f.startswith(problem) and f.endswith(".tc")]

os.system('clear')
for testcase in sorted(testcases):
    print('[+]', colors.green+ "Running testcase %s" % testcase, colors.end)
    os.system('cat "problems/%s" | python problems/%s.py' % (testcase, problem))
    print('')