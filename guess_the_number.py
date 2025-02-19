import random

def play_guess_the_number():
    def guess_number():
        while True:
            try:
                min_number = int(input("Enter the minimum number: "))
                max_number = int(input("Enter the maximum number: "))
                attempts = int(input("Enter the number of attempts: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        target_number = random.randint(min_number, max_number)

        while attempts > 0:
            while True:
                try:
                    guess = int(input(f"Guess a number between {min_number} and {max_number}: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

            if guess == target_number:
                print("You won!")
                return

            print("You lost! Try again.")
            attempts -= 1
            print(f"Remaining attempts: {attempts}")

        print("You have reached the maximum number of attempts.")
        print("The target number was", target_number)

    guess_number()

    play_again = input("Do you want to continue with the game? [1] Yes, [2] No: ")
    while play_again not in ['1', '2']:
        print("Invalid input! Please enter [1] to continue with the game, or [2] to exit.")
        play_again = input("Do you want to continue with the game? [1] Yes, [2] No: ")

    if play_again == '1':
        play_guess_the_number()

play_guess_the_number()