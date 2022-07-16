#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      ASUS
#
# Created:     16-07-2022
# Copyright:   (c) ASUS 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

num=int(input("enter a number"))
factorial = 1
for i in range(1,num+1):
    factorial=factorial*i
print(f"factorial of {num} is {factorial} ")