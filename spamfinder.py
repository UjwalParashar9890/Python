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

text=input("enter a text")

if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("subscribe this"in text):
    spam= True
elif("click this" in text):
    spam= True
else:
    spam=False

if(spam):
    print("THIS TEXT IS SPAM")

else:
    print("THIS TEXT IS NOT SPAM")


