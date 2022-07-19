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
    #if two values are equal,declare a tie !
    if comp==you:
        return None
    #chose for all possibilities when computer choose 's'
    elif comp=='s':
        if you=='w':
            return False
        if you=='g':
            return True
        #choose for all possibilities when computer choose 'w'
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
        #choose for all possibilities when computer choose 'g'
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

#now check for computer's turn!

print("comp turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

#now check for your's turn!

you=input("your turn: Snake(s) Water(w) or Gun(g)?")
a=gameWin(comp,you)

#print what both the sides have choosen!

print(f"computer chose {comp}")
print(f"you chose {you}")

if a==None:
    print("The Game is a tie!")
elif a:
    print("You Win! Hurray!!!!!")
else:
    print("Sorry! You Lose")

