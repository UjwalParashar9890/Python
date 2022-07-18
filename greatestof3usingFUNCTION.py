#-------------------------------------------------------------------------------
# Name:        module6
# Purpose:
#
# Author:      ASUS
#
# Created:     18-07-2022
# Copyright:   (c) ASUS 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m=maximum(2,6,7)
print(m)
