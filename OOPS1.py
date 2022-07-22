#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ASUS
#
# Created:     22-07-2022
# Copyright:   (c) ASUS 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class RailwayForm:
    formtype="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

ujwalsApplication=RailwayForm()
ujwalsApplication.name=input("enter your name!")
ujwalsApplication.train="rajdhani express"
ujwalsApplication.printData()