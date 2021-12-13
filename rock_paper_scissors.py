import random
'''I am going to define a function that the program will use to produce 
pseudo-random result .
''' 
choice_list = ["Scissors", "Rock", "Paper"]
def programs_pick():
    return random.choice(choice_list) 

test = programs_pick()
print(test)
print("\t\t\t\tWe are going to play a game of rock, paper and scissors\n\n")
print("\t\t\t\t\t\t\tHave fun\n")

your_score = int()
progam_score = int()

while True:
    program_choice = programs_pick().upper()
    your_choice = input("Pick among (ROCK, PAPER SCISSORS): ").upper()
    if your_choice == "ROCK" and program_choice == "PAPER":
        print(f'I picked {program_choice}')
        print("You Lost!!!")

    elif your_choice == "ROCK" and program_choice == "SCISSORS":
        print(f'I picked {program_choice}')
        print("You Won!!!")
        your_score += 1

    elif your_choice == "ROCK" and program_choice == "ROCK":
        print(f"I picked {program_choice}")
        print("It's a draw :) ")

    elif your_choice == "SCISSORS" and program_choice == "SCISSORS":
        print(f"I picked {program_choice}")
        print("It's a draw :) ")

    elif your_choice == "SCISSORS" and program_choice == "ROCK":
        print(f"I picked {program_choice}")
        print("You lost!!!")

    elif your_choice == "SCISSORS" and program_choice == "PAPER":
        print(f"I picked {program_choice}")
        print("You won!!!")
        your_score += 1

    elif your_choice == "PAPER" and program_choice == "PAPER":
        print(f"I picked {program_choice}")
        print("It's a draw :) ")

    elif your_choice == "PAPER" and program_choice == "ROCK":
        print(f"I picked {program_choice}")
        print("You won!!!")
        your_score += 1

    elif your_choice == "PAPER" and program_choice == "SCISSORS":
        print(f"I picked {program_choice}")
        print("you lost!!")
    
    to_continue = input("Do you want to continue?(yes/no) ").lower()
    if to_continue == "yes":
        continue
    else:
        break
print(f"your score: {your_score}")
if your_score > 1:
    print("You won the game")
else:
    print("Too BAD, you lost the game")
