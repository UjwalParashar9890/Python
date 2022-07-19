#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ASUS
#
# Created:     19-07-2022
# Copyright:   (c) ASUS 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def sum(n):
    if n<=1:
        return 1
    return n + sum(n-1)

f=sum(5)
print(f)