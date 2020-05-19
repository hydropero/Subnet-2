import string
import sys
import random
import cidr_dec_conv
from tkinter import *


def questionCreationFunc():

    generatedcirdlist= []


    for i in range(0, 10):
        count = 0
        randCidrGenerator = random.randint(10, 32)
        x = randCidrGenerator
        y = cidr_dec_conv.cidrconvert(x)
        generatedcirdlist.append([x, y])

        count += 1
    print(generatedcirdlist)



questionCreationFunc()

def test():
    return cidrcalculator()

def test2():
    print("Apparently works fine now")


def test5():
    print("Starting the test!")

    print("Quick what is /" + str(randCidrGenerator) + "in decimal form")
def startup():

    starter = True
    while starter:
        print("Welcome to the IP Addressing/Subnetting Tool")
        intro = str(input("Would you like to get started? Y / N: "))
        intro = intro.upper()
        if intro == 'Y':
            print("Great let's begin!")
            optionsmenu()
        elif intro == 'N':
            print("Sorry to hear that, maybe next time!")
            sys.exit()
        else:
            print("Invalid option, please try again")

def optionsmenu():
    print("we're now in the options menu function")
    starter = True
    while starter:

        print("Please select a tool from the options below\n")
        print("For an in depth subnetting tutorial select ---------------------------> [1]")
        print("To perform a CIDR to decimal subnet conversion or vice versa select --> [2]")
        print("To determine network/subnet boundaries select ------------------------> [3]")
        print("To request subnetting practice questions select ----------------------> [4]")
        print("To run the subnetting gauntlet select --------------------------------> [5]")
        switch_answer = input("Please enter your selection here: ")

        switcher = {
            "1": "test",
            "2": test,
            "3": test2,
            "4": "test4",
            "5": test5


        }

        switcher[switch_answer]()








def cidrcalculator():

    starter = True
    while starter:
        print("-------------------------------------------------------------------------------------------------------")
        print("Welcome to the subnet converter")
        form = int(input("CIDR --> Decimal notation [1] \nDecimal notation --> CIRD [2]: \nReturn to main menu [3]"))
        if form == 1:
            cidr = int(input("Please enter CIDR number /"))
            cidr_dec_conv.cidrconvert(cidr)
        elif form == 2:
            decimal = input("Please enter subnet mask in decimal notation:")
            cidr_dec_conv.dec_convert(decimal)
        elif form == 3:
            optionsmenu()
        else:
            print("Invalid option, please try again")





startup()



