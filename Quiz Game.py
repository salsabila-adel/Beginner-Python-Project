# Quiz Game

questions=("what is the capital of Egypt?",
           "what are colors of Egypt Flag?",
           "what is the biggest animal in the world?",
           "How many players in Football Team?",
           "What is the Programming Lan. used in that Program? ")

options=(("A. Alexandria","B. Luxor","C. Cairo","D. Mexico"),
         ("A. Red,White,black","B. Yellow,Orange,Blue","C. Black,Blue,Red","D. Pink,Orange,Black"),
         ("A. Elephant","B. Dinosaur","C. Blue Whale","D. Chimpanzee"),
         ("A. 14","B. 21","C. 45","D. 11"),
         ("A. C++","B. Java","C. Python","D. VHDL"))

answers=("C","A","C","D","C")
guesses=[]
score=0
question_num=0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter your Choice: ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("Correct!")
    else:
        print("Wrong!")
        print(f" The Correct Answer is : {answers[question_num]}")

    print("***************************")
    question_num+=1

print()
print("***************************")
print("        ✨RESULTS✨        ")
print("***************************")

print("Answers: ",answers)
print("Guesses: ",guesses)


print()
score=(score/len(questions))*100
print(f"💯 Your Score is : {score}%")