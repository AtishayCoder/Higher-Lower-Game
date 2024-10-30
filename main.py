import random

# Get number
number = random.randint(1, 100)
lives = 5

# While loop
while True:
    guess = int(input("Enter your guess: \n"))
    if lives == 1:
        print("You ran out of lives!")
        break
    else:
        if number == guess:
            print(f"You got it! The number was {number}.")
            break
        elif number > guess:
            lives -= 1
            print(f"Your guess is lower than the actual number. You have {lives} lives remaining. Try again!")
        elif number < guess:
            lives -= 1
            print(f"Your guess is higher than the actual number. You have {lives} lives remaining. Try again!")
