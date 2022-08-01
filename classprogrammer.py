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

class Programmer:
    company="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getInfo(self):
        print(f"The name of the {self.company} Programmer is {self.name} and he/she is working in the {self.product} product")

ujwal=Programmer("Ujwal","Skype")
tushar=Programmer("Tushar","GitHub")
ujwal.getInfo()
tushar.getInfo()
