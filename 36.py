import random
number = random.randint(1, 10)
guess = int(input("Enter a number: "))
while guess != number:
    if guess < number:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Enter a number: "))
print("You guessed it")