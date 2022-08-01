#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ASUS
#
# Created:     01-08-2022
# Copyright:   (c) ASUS 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Calculator:
    def __init__(self,num):
        self.number=num

    def square(self):
        print(f"The square of {self.number} is {self.number**2}")

    def cube(self):
        print(f"The cube of {self.number} is {self.number**3}")

    def squareRoot(self):
        print(f"The squareRoot of {self.number} is {self.number**0.5}")

b=int(input("please enter a number"))
a=Calculator(b)
a.square()
a.cube()
a.squareRoot()