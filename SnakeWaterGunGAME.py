#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ASUS
#
# Created:     20-07-2022
# Copyright:   (c) ASUS 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        if you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("comp turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

you=input("your turn: Snake(s) Water(w) or Gun(g)?")
a=gameWin(comp,you)

print(f"computer chose {comp}")
print(f"you chose {you}")

if a==None:
    print("The Game is a tie!")
elif a:
    print("You Win! Hurray!!!!!")
else:
    print("Sorry! You Lose")

