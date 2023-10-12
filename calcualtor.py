import sys
import random
import time
import math

def main():
    answer = input("----------------------------------\n Welcome to the pyhton calculator \n 1.ADD \n 2.SUBTRACT \n 3.MULTIPLY \n 4.DIVIDE \n 5.POWER \n 6.SQUARE ROOT \n 7.EXIT \n----------------------------------\n")
    if answer == "1" or answer.upper() == "ADD":
        add()
    elif answer == "2" or answer.upper() == "SUBTRACT":
        subtract()
    elif answer == "3" or answer.upper() == "MULTIPLY":
        multi()
    elif answer == "4" or answer.upper() == "DIVIDE":
        div()
    elif answer == "5" or answer.upper() == "POWER":
        power()
    elif answer == "6" or answer.upper() == "SQUARE ROOT":
        square_root()
    elif answer == "7" or answer.upper() == "EXIT":
        print("BYE")
        sys.exit
    else:
        print("INVALID\nTRY AGAIN...")
        main()

def add():
    quantity = int(input("How many numbers do you want to add?"))
    score = 0
    total = 0
    average = 0
    while quantity > score :
        number = int(input("what is your number?"))
        score = score + 1
        total = total + number
    rounding(total)
    escape()

def subtract():
    quantity = int(input("How many numbers do you want to subtract?"))
    score = 0
    total = 0
    while quantity > score :
        number = int(input("what is your number?"))
        score = score + 1
        if score == 1:
            total = number
        else:
            total = total - number
    rounding(total)
    escape()

def multi():
    quantity = int(input("How many numbers do you want to multiply?"))
    score = 0
    total = 1
    average = 0
    while quantity > score :
        number = int(input("what is your number?"))
        score = score + 1
        total = total*number
    rounding(total)
    escape()

def div():
    quantity = int(input("How many numbers do you want to divide?"))
    score = 0
    total = 0
    average = 0
    while quantity > score :
        number = int(input("what is your number?"))
        score = score + 1
        if score == 1:
            total = number
        else:
            total = total/number
    rounding(total)
    escape()
    
def power():
    num = int(input("What is your number?"))
    power = int(input("What is the power?"))
    score = 0
    total = pow(num,power)
    rounding(total)
    escape()

def square_root():
    num = int(input("What is your number?"))
    score = 0
    total = math.sqrt(num)
    rounding(total)
    escape()

def escape():
    escape = input("Do you want to go back to the main menu(M) or leave(L)")
    if escape.upper() == "M":
        print("Going to main menu...")
        main()
    elif escape.upper() == "L":
        print("Exiting program...")
        sys.exit()
    else:
        print("Invalid Input\nGoing to menu...")

def rounding(total):
    answer = input("Do you want your answer rounded? Y/N ")
    if answer.upper() == "Y":
        num = int(input("How many decimal places?"))
        total = round(total,num)
        print(total)
    elif answer.upper() == "N":
        print(total)
    else:
        print("INVALID...\n TRY AGAIN")
        rounding()

main()