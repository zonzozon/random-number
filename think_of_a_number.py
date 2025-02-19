import random

def play_think_of_a_number():
    def play_game():
        while True:
            try:
                min_number = int(input("Enter the minimum number: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        while True:
            try:
                max_number = int(input("Enter the maximum number: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        while True:
            try:
                max_attempts = int(input("Enter the maximum number of attempts: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        target_number = random.randint(min_number, max_number)
        attempts = 0

        while attempts < max_attempts:
            attempts += 1
            guess = input(f"Is {target_number} your number? [y/n]: ")

            while not guess.lower() in ['y', 'n']:
                print("Invalid input! Please enter 'y' or 'n'.")
                guess = input(f"Is {target_number} your number? [y/n]: ")

            if guess.lower() == 'y':
                print("I guessed your number!")
                return

            print(f"Remaining attempts: {max_attempts - attempts}")

            available_numbers = list(range(min_number, max_number + 1))
            available_numbers.remove(target_number)
            target_number = random.choice(available_numbers)

        print("I have exhausted my attempts.")
        user_number = input("What was the number? ")

        while not user_number.isdigit():
            print("Invalid input! Please enter a valid number.")
            user_number = input("What was the number? ")

        user_number = int(user_number)

        if user_number == target_number:
            print("You entered the number you previously indicated was not correct.")
            print("The game ends.")
        elif user_number > max_number:
            print("The number you entered is greater than the maximum number.")
            print(f"The maximum number was {max_number}.")
        elif user_number < min_number:
            print("The number you entered is less than the minimum number.")
            print(f"The minimum number was {min_number}.")
        else:
            print("Good Game")

    while True:
        play_game()

        play_again = input("Do you want to continue playing? [1: Yes, 2: No]: ")

        while play_again not in ['1', '2']:
            print("Invalid input! Please enter either 1 or 2.")
            continue_game = input("Do you want to continue playing? [1: Yes, 2: No]: ")

        if play_again == '1':
            play_think_of_a_number()

play_think_of_a_number()