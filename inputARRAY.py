#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ASUS
#
# Created:     09-07-2022
# Copyright:   (c) ASUS 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from array import *
arr=array('i',[])
n=int(input("enter the length of the array: "))

for i in range(n):
    x=int(input("enter the next value"))
    arr.append(x)

print(arr)