import random
import string
import sys

from sympy.codegen import Print

print("Hi")

comp_array_guess=['ROCK','PAPER','SCISSOR']

Lives=2
Human_Choice=""

while( Lives!=0):
    rand_choice = (random.choice(comp_array_guess))
    Human_Choice=input("Enter Rock . Paper ,Scissors:")
    Human_Choice.isupper()
    print("Computer Says",rand_choice)
    if(rand_choice =="ROCK" and Human_Choice =="SCISSOR"):

        print("You Lost")
        Lives-=1
    elif (rand_choice == "SCISSOR" and Human_Choice == "ROCK"):
        print("You Win")
    elif (rand_choice == "PAPER" and Human_Choice == "SCISSOR"):
        print("You Win")
    elif (rand_choice == "SCISSOR" and Human_Choice == "PAPER"):
        print("You Lost")
        Lives -= 1
    elif (rand_choice == "ROCK" and Human_Choice == "PAPER"):
        print("You WIN")
    elif (rand_choice == "PAPER" and Human_Choice == "ROCK"):
        print("You LOSE")
        Lives -= 1
    elif(rand_choice==Human_Choice):
        print("Both Got Same , Try Again")

    else:
        print("You didnt typed ROCK/PAPER/SCISSORS")
    if(Lives==0):
        print("Game Over")










def bubbleSort(array):
    swap=True
    n=len(array)
    while swap:
        swap=False

        for i in range(n-1):
            if array[i] > array[i+1]:
                temp=array[i]
                array[i]=array[i+1]
                array[i+1]=temp
                swap=True




    print(array)
    return array

#bubbleSort([3,6,4,7,8])

print("x\ub002")
print("0=ax\u002b2+bx+c")



