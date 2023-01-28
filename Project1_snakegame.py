import random
from re import S
from tkinter import W
def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you =='w':
            return False
        elif you == 'g':
            return True
        elif comp == 'w':
            if you =='g':
                return False 
            elif you == 's':
                return True
comp=input("Computer Turn:Snake(s) water(w) or gun(g)?")
randNo=random.randint(1,3)
print(randNo)
if randNo == 1:
    comp='s'
elif randNo == 2:
    comp='w'
elif randNo == 3:
    comp='g'



you=input("Player's Turn:Snake(s) water(w) or gun(g)?")
a=gamewin(comp,you)

print("Computer choose: ",comp)
print("You chose: ",you)
if a == None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print("You lost!!!")
