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

age=input("Hey Buddy! What is your age ?")
if int(age)<20:
    print("you are in school!")

elif int(age)<20 and int(age)>3:
    print("you are a kid!")

else:
    print("hey there!")