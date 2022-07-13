#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      ASUS
#
# Created:     13-07-2022
# Copyright:   (c) ASUS 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a=int(input("enter your marks!"))
if(a>90 and a<100):
    print("excellent")
if(a>80 and a<90):
    print("GRADE A!")
if(a>70 and a<80):
    print("GRADE B!")
if(a>60 and a<70):
    print("GRADE C!")
if(a>50 and a<60):
    print("GRADE D!")
else:
    print("SORRY! you are failed the exam")
