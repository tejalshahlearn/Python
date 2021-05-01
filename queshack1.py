#!/bin/python

import math
import os
import random
import re
import sys


# write your code here
def avg(*avgnum):
    for ele in range(0, len(avgnum)): 
        if(len(avgnum)<=1 and len(avgnum)<=100):
            if (avgnum[ele]>=-100 and avgnum[ele]<=100):
             sum_num = sum_num + t           
             avg = sum_num / len(avgnum)
    return avg
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = map(int, raw_input().split())
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
