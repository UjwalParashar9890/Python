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
        print(f"Salary of employee working in {self.company} is {self.salary}")

harry=Employee()
harry.salary = 100000
Employee.getSalary(harry)