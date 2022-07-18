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

def factorial_recursive(n):
    if n==0 or  n==1:
        return 1
    return n * factorial_recursive(n-1)

f=factorial_recursive(5)
print(f)