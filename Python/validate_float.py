# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

def validateFloat(number):
    if re.match(r"[-+]{0,1}\d*\.\d+$", number) is None:
        print "False"
    else: print "True"

T = int(raw_input().strip())
while T > 0:
    validateFloat(raw_input().strip())
    T -= 1
