import random

def guess_number():
    min_number = int(input("Enter the minimum number: "))
    max_number = int(input("Enter the maximum number: "))
    attempts = int(input("Enter the number of attempts: "))

    target_number = random.randint(min_number, max_number)

    while attempts > 0:
        guess = int(input(f"Guess a number between {min_number} and {max_number}: "))

        if guess == target_number:
            print("You won!")
            return

        print("You lost! Try again.")
        attempts -= 1

    print("You have reached the maximum number of attempts.")
    print("The target number was", target_number)

guess_number()
