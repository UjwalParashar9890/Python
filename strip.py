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

def replace_and_strip(string,word):
    newStr=string.replace(word, "")
    return newStr.strip()

this=" ujwal is a good boy"
n=replace_and_strip(this,"ujwal")
print(n)