#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    elevation = 0
    valleyCount = 0
    for step in path:
        if  step == "D": elevation-=1
        elif  step == "U":
            elevation+=1
            if not elevation: valleyCount+=1
    return valleyCount;






stepsTaken = "DDUUUUDD"
print(countingValleys(len(stepsTaken), stepsTaken))