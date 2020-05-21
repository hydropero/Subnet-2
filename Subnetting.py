import string
import sys
import random
import cidr_dec_conv
import re


switchreg = "[^1234a-z]+"


globallistscore = []

def questionCreationFunc():

    randCidrGenerator = random.randint(0, 32)
    x = randCidrGenerator
    y = cidr_dec_conv.cidrconvert(x)
    generatedcidrlist = [x, y]
    return generatedcidrlist  # format of list is [[32], [255.255.255.255]]


def textquestiongenerator():
    list = []
    a = "Quick, convert convert this number to the alternative notation -> "
    b = "Please convert to CIDR notation -> "
    c = "Convert to decimal -> /"
    list.append(a)
    list.append(b)
    list.append(c)
    choice = random.randint(0, 2)

    return list[choice]

def questionblendgenerator():
    text = textquestiongenerator()
    notation = questionCreationFunc()
    cnotation = notation[0]
    dnotation = notation[1]
    oneortwogen = random.randint(0, 1)
    rnotation = notation[oneortwogen]

    if text[0] == 'Q':
        if oneortwogen == 0:
            fullq = text + '/' + str(rnotation)
            print(fullq)
        else:
            fullq = text + str(rnotation)
            print(fullq)

        if oneortwogen == 0:
            answer1 = str(input("Enter your input here: "))
            if str(answer1) == str(dnotation):

                print('Correct!')
                globallistscore.append(1)
                return
            else:
                print('WRONG!')
                globallistscore.append(0)
                return
        else:
            answer1 = str(input("Enter your input here: /"))
            if str(answer1) == str(cnotation):
                print('Correct!')
                globallistscore.append(1)
                return
            else:
                print('WRONG!')
                globallistscore.append(0)
                return

    elif text[0] == 'P':
        fullqtwo = text + str(dnotation)
        print(fullqtwo)
        answer2 = input("Enter your input here: /")
        if str(answer2) == str(cnotation):
            print('Correct')
            globallistscore.append(1)
            return
        else:
            print('WRONG!')
            globallistscore.append(0)
            return

    elif text[0] == 'C':
        fullqthree = text + str(cnotation)
        print(fullqthree)
        answer3 = input("Enter your input here: ")
        if str(answer3) == str(dnotation):
            print('Correct')
            globallistscore.append(1)
            return
        else:
            print('WRONG!')
            globallistscore.append(0)
            return




def test():
    return cidrcalculator()

def test2():
    print("")

def test3():
    print("Apparently works fine now")


def test4():

    questionanswerpair = questionCreationFunc()


    print("Starting the test!")
    print('-------------------\n\n')
    for i in range(0, 10):
        questionblendgenerator()

    print(len(globallistscore))
def test5():
    print('anything else')


def startup():

    starter = True
    while starter:
        print("\nWelcome to the IP Addressing/Subnetting Tool\n")
        intro = str(input("Would you like to get started? Y / N: "))
        intro = intro.upper()
        if intro == 'Y':
            print("--------------------------------------------------------------------------")
            optionsmenu()
        elif intro == 'N':
            print("Sorry to hear that, maybe next time!")
            sys.exit()
        else:
            print("Invalid option, please try again")


def optionsmenu():
    starter = True

    while starter:

        print("Please select a tool from the options below\n")
        print("For an in depth subnetting tutorial select ---------------------------> [1]")
        print("To perform a CIDR to decimal subnet conversion or vice versa select --> [2]")
        print("To determine network/subnet boundaries select ------------------------> [3]")
        print("To run the subnetting gauntlet select --------------------------------> [4]")
        switch_answer = input("\nPlease enter your selection here: ")
        list = ['1', '2', '3', '4']
        if switch_answer not in list:
            print("\nInvalid selection please try again\n")
            optionsmenu()
        else:
            switcher = {
                "1": "test",
                "2": test2,
                "3": test3,
                "4": test4,
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



