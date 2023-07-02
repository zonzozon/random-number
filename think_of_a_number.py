import random

def play_think_of_a_number():
    min_number = int(input("Enter the minimum number: "))
    max_number = int(input("Enter the maximum number: "))
    max_attempts = int(input("Enter the maximum number of attempts: "))

    target_number = random.randint(min_number, max_number)
    attempts = 0

    while attempts < max_attempts:
        attempts += 1
        guess = input(f"Is {target_number} your number? [y/n]: ")

        if guess.lower() == 'y':
            print("I guessed your number!")
            return

    print("I have exhausted my attempts.")
    user_number = input("What was the number? ")

    while not user_number.isdigit():
        print("Invalid input! Please enter a valid number.")
        user_number = input("What was the number? ")

    user_number = int(user_number)

    if user_number > max_number:
        print("The number you entered is greater than the maximum number.")
        print(f"The maximum number was {max_number}.")
    elif user_number < min_number:
        print("The number you entered is less than the minimum number.")
        print(f"The minimum number was {min_number}.")
    else:
        print("You entered a number within the valid range.")

    continue_game = input("Do you want to continue with the game? [1: Yes, 2: No]: ")

    while continue_game not in ['1', '2']:
        print("Invalid input! Please enter either 1 or 2.")
        continue_game = input("Do you want to continue with the game? [1: Yes, 2: No]: ")

    if continue_game == '1':
        play_think_of_a_number()
    else:
        print("Thank you for playing!")

play_think_of_a_number()
