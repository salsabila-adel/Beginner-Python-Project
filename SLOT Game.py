# Slot Game
import random
import time



def spin_row():
    symbols =['🍒', '🍉', '🍋', '🔔' ,'⭐']
    results=[random.choice(symbols) for i in range(3)]
    return results

def print_row(row):
    print(" | ".join(row))

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet*3
        elif row[0] == '🍉':
            return bet*4
        elif row[0] == '🍋':
            return bet*5
        elif row[0] == '🔔':
            return bet*10
        elif row[0] == '⭐':
            return bet*20
        return None
    else:
        return 0


def main():
    # balance=500
    print("########################")
    print("Welcome to SLOT Game 🤑")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("#########################")

    balance=int(input("Enter your Balance to Start the Game:😈"))

    while balance>0:
        print(f"Your Current Balance: L.E {balance}")


        try:
            bet=int(input("Enter your bet amount: "))
        except ValueError:
            print("Please enter a numeric value")
            continue


        if bet>balance:
            print("Insufficient Amount 😒")
            continue
        if bet<=0:
            print("The amount must be greater than 0")
            continue

        balance-=bet

        row=spin_row()
        # for icon in['⌛','⏳']*10:
        #     print(f"\rSpinning {icon}",end="",flush=True)
        #     time.sleep(0.2)
        spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

        for _ in range(3):
            for frame in spinner:
                print(f"\rSpinning {frame}", end="", flush=True)
                time.sleep(0.1)
        print("\r Spinning ✅")

        print_row(row)
        payout=get_payout(row,bet)
        if payout>0:
            print("Congratulations! You won🤑 ")
        else:
            print("Sorry, you lost this Round ☹️")

        balance+=payout


if __name__ == "__main__":
    main()