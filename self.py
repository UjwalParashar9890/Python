#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ASUS
#
# Created:     27-07-2022
# Copyright:   (c) ASUS 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Employee:
    company="Google"
    def getSalary(self):
        print("Salary is 100k")

harry=Employee()
Employee.getSalary(harry)