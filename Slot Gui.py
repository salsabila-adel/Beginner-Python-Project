# SLOT Game with GUI
# Slot Machine GUI using Tkinter

import tkinter as tk
import random


# ---------------- Logic ----------------

symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']


def spin_row():
    return [random.choice(symbols) for _ in range(3)]

def show_row(row):
    for i, symbol in enumerate(row):
        slot_labels[i].config(text=symbol)

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:

        if row[0] == '🍒':
            return bet * 3

        elif row[0] == '🍉':
            return bet * 4

        elif row[0] == '🍋':
            return bet * 5

        elif row[0] == '🔔':
            return bet * 10

        elif row[0] == '⭐':
            return bet * 20

    return 0



# ---------------- GUI ----------------

window = tk.Tk()
window.configure(bg="black")

balance = 0


# ---------------- Balance Input ----------------

balance_frame = tk.Frame(window)

balance_frame.pack(pady=20)


balance_title = tk.Label(
    balance_frame,
    text="Enter Starting Balance:",
    font=("Arial",15)
)

balance_title.grid(row=0, column=0, padx=10)


balance_entry = tk.Entry(
    balance_frame,
    font=("Arial",15),
    width=10
)

balance_entry.grid(row=0, column=1)


balance_message = tk.Label(
    window,
    text="",
    font=("Arial",12),
    bg="black",
    fg="red"
)

balance_message.pack()


def set_balance():

    global balance

    try:
        value = int(balance_entry.get())

        if value <= 0:
            balance_message.config(
                text="Balance must be greater than 0",
                fg="red"
            )
            return

        balance = value

        balance_label.config(
            text=f"Balance: L.E {balance}",
            fg="#FF4500",
            bg="black"
        )

        balance_entry.config(
            state="disabled"
        )

        start_balance_button.config(
            state="disabled"
        )

        balance_message.config(
            text="Game Started 🎰",
            fg="green"
        )

    except ValueError:

        balance_message.config(
            text="Enter a valid number ❌",
            fg="red"
        )


start_balance_button = tk.Button(
    balance_frame,
    text="Start Game 🎰",
    font=("Arial",12),
    command=set_balance,
    bg="gold"
)

start_balance_button.grid(
    row=1,
    column=0,
    columnspan=2,
    pady=15
)

window.title("🎰 Slot Machine")
window.geometry("600x500")
window.resizable(False, False)


spinning = False



window = tk.Tk()
window.configure(bg="black")

window.title("🎰 Slot Machine")
window.geometry("600x500")
window.resizable(False, False)



# Title

title = tk.Label(
    window,
    text="Welcome to SLOT Game 🤑",
    font=("Arial", 25, "bold"),
    fg="#FF4500"
)

title.pack(pady=20)



# Balance

balance_label = tk.Label(
    window,
    text=f"Balance: L.E 0",
    font=("Arial", 18),
    fg="#FF4500"

)

balance_label.pack()



# Slot display

slot_frame = tk.Frame(window)

slot_frame.pack(pady=40)



slot_labels = []

for i in range(3):

    label = tk.Label(
        slot_frame,
        text="❔",
        font=("Arial", 50),
        width=3
    )

    label.grid(row=0, column=i, padx=15)

    slot_labels.append(label)



# Bet Entry

bet_frame = tk.Frame(window)

bet_frame.pack()


bet_label = tk.Label(
    bet_frame,
    text="Bet Amount:",
    font=("Arial", 15)
)

bet_label.grid(row=0, column=0)



bet_entry = tk.Entry(
    bet_frame,
    font=("Arial",15),
    width=10
)

bet_entry.grid(row=0, column=1)



# Result message

result_label = tk.Label(
    window,
    text="",
    font=("Arial",18)
)

result_label.pack(pady=20)



# ---------------- Animation ----------------


spinner = [
    "⠋",
    "⠙",
    "⠹",
    "⠸",
    "⠼",
    "⠴",
    "⠦",
    "⠧",
    "⠇",
    "⠏"
]


spin_count = 0


def animate():

    global spin_count

    if not spinning:
        return

    frame = spinner[spin_count]

    for label in slot_labels:
        label.config(text=frame)

    spin_count += 1

    if spin_count >= len(spinner):
        spin_count = 0

    window.after(100, animate)



# ---------------- Spin Button ----------------


def spin():

    global balance
    global spinning


    if spinning:
        return


    try:
        bet = int(bet_entry.get())

    except ValueError:

        result_label.config(
            text="Enter a valid number ❌",
            fg="red"
        )

        return



    if bet <= 0:

        result_label.config(
            text="Bet must be greater than 0",
            fg="red"
        )

        return



    if bet > balance:

        result_label.config(
            text="Insufficient balance 😒",
            fg="red"
        )

        return



    balance -= bet

    balance_label.config(
        text=f"Balance: L.E {balance}"
    )


    spinning = True

    result_label.config(
        text="Spinning 🎰",
        fg="blue"
    )


    animate()


    # بعد 3 ثواني أظهر النتيجة

    window.after(
        3000,
        lambda: finish_spin(bet)
    )




def finish_spin(bet):

    global balance
    global spinning

    # إيقاف الـ loading أولًا
    spinning = False

    # اختيار النتيجة
    row = spin_row()

    # عرض النتيجة
    for i in range(3):
        slot_labels[i].config(text=row[i])


    payout = get_payout(row, bet)


    if payout > 0:

        balance += payout

        result_label.config(
            text=f"You won 🤑 +{payout} L.E",
            fg="green"
        )

    else:

        result_label.config(
            text="You lost this round ☹️",
            fg="red"
        )


    balance_label.config(
        text=f"Balance: L.E {balance}"
    )



# Button

spin_button = tk.Button(
    window,
    text="SPIN 🎰",
    font=("Arial",20,"bold"),
    command=spin,
    bg="gold"
)

spin_button.pack(pady=20)



window.mainloop()