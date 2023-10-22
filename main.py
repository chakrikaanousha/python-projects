import random

def play():
    print("r: rock \n p: paper \n s:scissors")
    user = input("enter your choice: ")
    comp = random.choice(["r","p","s"]) #random function [ number of inputs given ]
    print("comp input: "+comp)

    if(user==comp):
        print("It's a Tie!!")
    #
    elif(user=='r' and comp =="p" or user=='s' and comp =='r' or user =="p" and comp=='s'):
        print("you loose!")
    else:
        print("you win")


play()
