import random

num = random.randint(1, 10)

tries = 0

while True:
    guess = int(input("Please guess your Number between 1 - 10 :- "))
    if guess == num:
        tries += 1
        print(f"Your guess is right in {tries} tries. ")
        break
    elif guess < num :
        print("Litter higher. ")
        tries += 1
    elif guess > num :
        print("Little lower: ")
        tries += 1
    else :
        print("You guess the wrong answer: ")