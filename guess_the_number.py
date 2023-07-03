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

        continue_game = input("Do you want to continue with the game? [1: Yes, 2: No]: ") 
  
     while continue_game not in ['1', '2']: 
         print("Invalid input! Please enter either 1 or 2.") 
         continue_game = input("Do you want to continue with the game? [1: Yes, 2: No]: ") 
  
     if continue_game == '1': 
         play_guess_the_number() 
     else: 
         print("Thank you for playing!")

play_guess_user_number()