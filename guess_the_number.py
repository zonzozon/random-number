import random

def play_guess_user_number():
    def guess_number():
        min_number = int(input("Enter the minimum number: "))
        max_number = int(input("Enter the maximum number: "))
        attempts = int(input("Enter the number of attempts: "))

        target_number = random.randint(min_number, max_number)

        while attempts > 0:
            guess = int(input(f"Guess a number between {min_number} and {max_number}: "))

            if guess == target_number:
                print("You won!")
                return True

            print("You lost! Try again.")
            attempts -= 1

        print("You have reached the maximum number of attempts.")
        print("The target number was", target_number)
        return False

    while True:
        if guess_number():
            break

        play_again = input("Do you want to continue with the game? [1] Yes, [2] No: ")
        while play_again not in ['1', '2']:
            print("Invalid input! Please enter [1] to continue with the game, or [2] to exit.")
            play_again = input("Do you want to continue with the game? [1] Yes, [2] No: ")

        if play_again == '2':
            print("Thank you for playing!")
            break

play_guess_user_number()