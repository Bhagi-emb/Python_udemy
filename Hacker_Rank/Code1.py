#!/bin/python3

import math #math is for math functions
import os #os is for operating system functions
import random #random is for random number generation
import re #re is for regular expressions
import sys #sys is for system functions

#__main__ is a special variable that is set to the name of the module
#_name_ is a special variable that is set to the name of the module
if __name__ == '__main__': 
    n = int(input().strip())  
    #strip() is used to remove any leading or trailing whitespace
    #int() is used to convert the input to an integer
    #input() is used to take input from the user

#below is the solution for the problem    
if n%2 == 0 :
    if n>2 and n<5 :
        print("Not Weird")
    elif(n>6 and n <20) :
        print("Weird")
    else :
        print("Not Weird")
    
else :
    print("Weird")