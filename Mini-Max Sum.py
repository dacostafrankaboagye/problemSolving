'''
Hacker rank1


Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.


'''



#__________________________________________


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    # get the sum of arr
    #loop through and subtract the individual numbers
    #keep track of the min and the max
    theHighest = sum(arr)
    val = 0
    theMax, theMin = arr[0],theHighest
    for i in range(len(arr)):
        val = theHighest - arr[i]
        if val > theMax:
            theMax = val
        if val < theMin:
            theMin = val
    print(theMin, theMax)
            
        
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
