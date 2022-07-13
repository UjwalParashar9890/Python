#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ASUS
#
# Created:     13-07-2022
# Copyright:   (c) ASUS 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))
num3=int(input("enter your third number:"))
num4=int(input("enter your fourth number:"))

if(num1>num4):
    f1=num1
else:
    f1=num4
if(num2>num3):
    f2=num2
else:
    f2=num3
if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")
