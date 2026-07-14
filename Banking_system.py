# Banking System
import sys
from unittest import case


def show_balance(balance):
    print(f"Your current balance is L.E {balance}")


def deposit():
    dep=int(input("Enter your deposit amount: "))
    if dep<0:
        print("Invalid deposit amount")
        return 0
    else:
        return dep

def withdraw(balance):
    drawen=int(input("🤑Enter your withdraw amount: "))
    if drawen>balance:
        print("Invalid deposit amount😒")
        return 0
    elif drawen<0:
        print("The amount must be greater than 0 🙂")
        return 0
    else:
        return drawen

def main():
    balance = 0
    is_running=True

    while is_running:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("     Al-Ahly Banking System      ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()

            print("1-Show Balance\n2_Deposit\n3_Withdraw\n4-Exit")
            choice = int(input("Enter your choice 🫣: "))
            match choice:
                case 1:
                    show_balance(balance)
                case 2:
                    balance+=deposit()
                case 3:
                    balance-=withdraw(balance)
                case 4:
                    is_running=False
                case _:
                    print("Invalid choice 🙎")

    print("✨Thank you for using Banking System, Have a good day!☺️")
if __name__ == "__main__":
    main()
