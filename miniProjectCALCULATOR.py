#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      ASUS
#
# Created:     09-07-2022
# Copyright:   (c) ASUS 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#building a mini calculator project
first=input("enter your first number:")
operator=input("enter operator(+,-,*,/,%)")
second=input("enter your second number:")

first=int(first)
second=int(second)
if operator=="+":
    print(first+second)

elif operator=='-':
    print(first-second)

elif operator=='*':
    print(first*second)

elif operator=="/":
    print(first/second)

elif operator=='%':
    print(first%second)

else:
    print("INVALID OPERATION")

