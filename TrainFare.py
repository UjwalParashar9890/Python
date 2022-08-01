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

class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print(f"The name of the tarin is {self.name}")
        print(f"Available seats in the train are {self.seats}")

    def getFareinfo(self):
        print(f"The fare of the train is Rs.{self.fare}")

intercity=Train("Intercity Express:14019",90,300)
intercity.getStatus()
intercity.getFareinfo()
