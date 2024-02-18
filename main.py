import random
from art import logo


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
print(f"Pssst, the correct answer is {number}")

lives = 0


def difficulty():
    choose_difficulty = input(
        "Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choose_difficulty == "easy":
        return lives + 10
    else:
        return lives + 5


def compare(guess, number):
    if guess > number:
        print("Too high.")
    else:
        print("Too low.")

    print("Guess again.")


def game():
    lives = difficulty()
    end = False
    while not end:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if lives == 1 and guess != number:
            print("You've run out of guesses, you lose.")
            end = True
        elif guess != number:
            lives -= 1
            compare(guess, number)
        else:
            print(f"You got it! The answer was {guess}.")
            end = True


game()
