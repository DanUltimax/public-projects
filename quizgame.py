import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Back.BLUE + "   _=========_  ")
print(Back.BLUE + """//| QUIZ GAME |\\\\""")
print(Back.BLUE + "|||___________|||")

if input("Are you ready to play? \n").strip().lower() == "yes":
    print("Begin!\n")
else:
    print('Goodbye!')
    quit()

points = 0


def correct(sentence):
    global points
    global num_questions
    points += 1
    print(Fore.GREEN + f"\nCorrect! {sentence}")
    print(Fore.GREEN + f"You now have {points} point(s). {points}/{num_questions} correct!")

def incorrect():
    print(Fore.RED + f"\nIncorrect! You currently have {points} point(s). {points}/{num_questions} correct!")


num_questions = int(input("How many questions would you like to be asked? (1 - 7) \n"))



for i in range(num_questions):

    q1 = input(Fore.MAGENTA + """When was python first concieved?
            a. 1997
            b. 1989
            c. 2005
            d. 1974 \n \n""")

    if q1 == "b":
        correct("Python was first concieved by Guido van Rossum.")          #output: Correct! Python was first concieved by Guido van Rossum.
    else:
        incorrect()

    i += 1
    if i == num_questions:          #Checks if the current question corresponds with the amount of questions the user has chosen to answer.
        break                       #if the amount of questions have been answered, the quiz will end.

    q2 = input(Fore.MAGENTA + """\nWhich of the following is NOT a coding language?
            a. C#
            b. Rust
            c. Swift
            d. React \n \n""")

    if q2 == "d":
        correct("React.JS is a popular JavaScript coding library.")
    else:
        incorrect()

    i += 1
    if i == num_questions:
        break

    q3 = input(Fore.MAGENTA + """\nWho created the Linux operating system?
            a. Jordan Hubbard
            b. Linus Sebastian
            c. Linus Torvalds
            d. Michael Robertson \n \n""")

    if q3 == "c":
        correct("Linus Torvalds created the first instance of Linux in 1991 under open source code!")
    else:
        incorrect()

    i += 1
    if i == num_questions:
        break

    q4 = input(Fore.MAGENTA + """\nWhich of these games were coded in Python?
            a. Battlefield 2
            b. Cuphead
            c. Mega Man 11
            d. Titanfall \n \n""")

    if q4 == "a":
        correct("The 2005 game uses Python for many of its assets, including add-ons and functionality.")
    else:
        incorrect()

    i += 1
    if i == num_questions:
        break

    q5 = input(Fore.MAGENTA + """\nTrue or false: Men dominated the profession of a computer programmer in the 1960s.
            a. True
            b. False \n \n""")

    if q5 == "b":
        correct("Before computers were largely commercialized, women were more likely to work in technology for a variety of roles.")
    else:
        incorrect()

    i += 1
    if i == num_questions:
        break

    q6 = input(Fore.MAGENTA + """\nHalf Life 2 is one of the most significant PC games ever made. What game engine was it made in?
            a. Unreal Engine 2
            b. Source Engine
            c. Serious Engine \n \n""")

    if q6 == "b":
        correct("Other games made with Source include Counter Strike, Portal, and Garry's Mod.")
    else:
        incorrect()

    i += 1
    if i == num_questions:
        break

    q7 = input(Fore.MAGENTA + """\nWhat is the oldest programming language?
            a. C
            b. Basic
            c. SQL
            d. Fortran \n \n""")

    if q7 == "d":
        correct("Fortran was concieved back in 1957 by John Backus. Today it is considered a low-level language.")
    else:
        incorrect()

    i += 1
    if i == num_questions:
        break


print(f"Thank you for playing! \n You answered {num_questions}/7 questions!")
print(Fore.GREEN + f"Your final score is {points}/{num_questions} ({points / num_questions * 100:.1f}%).")