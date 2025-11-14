from random import choice

word=str(input("enter among rock,paper and scissors"))
computer=["rock","paper","scissors"]
randomthings=choice(computer)
if (word==randomthings):
    print(f"your input: {word}")
    print(f"computer's input: {randomthings}")
    print("it's a tie")
elif(word=="rock" and randomthings=="scissors"):
    print(f"your input: {word}")
    print(f"computer's input: {randomthings}")
    print("you won")
elif(word=="rock" and randomthings=="paper"):
    print(f"your input: {word}")
    print(f"computer's input: {randomthings}")
    print("you lose")
elif(word=="paper"and randomthings=="scissors"):
    print(f"your input: {word}")
    print(f"computer's input: {randomthings}")
    print("you lose")
elif(word=="paper"and randomthings=="rock"):
    print(f"your input: {word}")
    print(f"computer's input: {randomthings}")
    print("you won")
elif(word=="scissors"and randomthings=="rock"):
    print(f"your input: {word}")
    print(f"computer's input: {randomthings}")
    print("you lose")
elif(word=="scissors"and randomthings=="paper"):
    print(f"your input: {word}")
    print(f"computer's input: {randomthings}")
    print("you won")