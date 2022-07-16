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
prime = True
for i in range(2,num):
    if(num%i==0 and num!=2):
        prime = False
        break
if prime:
    print("this is a prime number")
