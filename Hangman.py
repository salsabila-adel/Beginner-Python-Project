# HangMan Game
import random

word=("apple","banana","strawberry","coconut","watermelon","orange","mango")

hangman_art={0:("   ",
                "   ",
                "   "),
             1:(" o ",
                "   ",
                "   "),
             2:(" o ",
                " | ",
                "   "),
             3: (" o ",
                 "/| ",
                 "   "),
             4: (" o ",
                 "/|\\",
                 "   "),
             5: (" o ",
                 "/|\\",
                 "/  "),
             6: (" o ",
                 "/|\\",
                 "/ \\")
             }

#_to_check_that_your_dictionary_is_working
# -----------------------------------------------
# for part in hangman_art:
#     for part_part in hangman_art[part]:
#         print(part_part)

def display_man(wrong_guesses):
    print("******************************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("******************************")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    print("🥝🍊🍉🥭🍍🍌🍓🍒🍑🍐🍏🫐🥑")
    print("      Welcome to Hangman!     ")
    print(" GUESS THE FRUIT AND WIIIIIIN ")
    print("🥝🍊🍉🥭🍍🍌🍓🍒🍑🍐🍏🫐🥑")
    answer=random.choice(word)
    hint=["_"]*len(answer)

    wrong_guesses=0
    guessed_letters=set()
    is_running=True

    while is_running:
        display_hint(hint)

        guess=input("Enter a Letter: ").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("بقلك اكتب حرف يا احول 😒")
            continue
        if guess in guessed_letters:
            print("كتبته قبل كدة بطّل فزلكة 😏")
            continue
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
        else:
            wrong_guesses+=1

        display_man(wrong_guesses)

        if wrong_guesses==6:
            print("\n")

            print("the Answer is: ",end="")
            display_answer(answer)
            print("❌❌❌❌❌ You LOSS ❌❌❌❌❌")
            break


        if "_" not in hint:
            # display_man(wrong_guesses)
            display_answer(answer)
            print("******** You WIN 🤩🤩 ********")
            is_running=False

if __name__ == "__main__":
    main()








