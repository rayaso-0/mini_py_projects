# Financing and Budget Application
from ast import Break
import time

balance = 0

def typing_animation():
    print(i, end="",flush=True)
    time.sleep(0.03)

# def goodbye():
#    goodbye = ("Thank you for using our services. Have a nice day!")
#    for i in str(goodbye):
#        typing_animation()



print("======================================")
user = input("Hello. Enter your username: ")
welcome = ("\nWelcome " + user + "!\n")
for i in str(welcome):
    typing_animation()
print("\n======================================")

while True:
    choice = input("What would you like to do today?\n1. Check Balance\n2. Add Income\n3. Subtract Expense\n4. Budget Application\nEnter Input: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            print("\nYour balance is", balance,".")
            choice1 = input("\nWould you like to do another action? (y/n): ")
            if choice1 != "y":
                goodbye = ("Thank you for using our services. Have a nice day!")
                for i in str(goodbye):
                    typing_animation()
                break
            else:
                choice1 = False
    else:
        retry = ("Please input a valid input and try again.")
        for i in str(retry):
                typing_animation()

        

