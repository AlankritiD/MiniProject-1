#Rolling Dice Simulator
import random
import sys
def dice_rolls(dice,sides):
    roll=[]
    
    for i in range(0,dice):
        face=random.randint(1,sides)
        roll.append(face)
    return roll 
dice= int(input("No. of Dice to be Rolled:"))
if (dice<=0):
    print("At least one dice should be rolled, Please try again")
    quit()
sides= int(input("Enter the no. of sides:"))
if(sides<=0):
    print("Must have atleast one side")
    quit()
roll=dice_rolls(dice,sides)

print(roll)
    
  
