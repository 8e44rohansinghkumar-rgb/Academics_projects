import random

lowest_num=0
highest_num=100
guesses=0
answer=random.randint(lowest_num,highest_num)
is_running=True

print("-------number guessing game--------")

while is_running:
    guess=input("enter your guess---")
    if(guess.isdigit()):
        guess=int(guess)
        guesses+=1
        if(guess<lowest_num or guess>highest_num):
             print("GUESS NUMBER NOT IN RANGE!")
             print(f"PLEASE ENTER YOUR NUMBER BETWEEN: {lowest_num} and {highest_num :}")
        elif(guess<answer):
             print("TOO LOW!")
        elif(guess>answer):
             print("TOO HIGH!")
        else:
             print(f"CORRECT! THE NUMBER WAS -{answer}")
             print(f"THE NUMBER OF GUESSES- {guesses}")
             is_running=False
    else:
        print("INVALID INPUT!")
        print(f"PLEASE ENTER YOUR NUMBER BETWEEN: {lowest_num} and {highest_num :}")