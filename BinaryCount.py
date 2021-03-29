#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    str1=""
    while n>=1:
        str1= str1+str(n%2)
        n=n//2
    ans=str1.split("0")
    max=0
    for i in range(0,len(ans)):
        if len(ans[i])>max:
            max=len(ans[i])
    print(max)
            
