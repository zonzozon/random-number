import random 
  
 def play_guess_the_number(): 
     def guess_number(): 
         while True: 
             min_number = input("Enter the minimum number: ") 
             if not min_number.isdigit(): 
                 print("Invalid input! Please enter a valid number.") 
                 continue 
  
             max_number = input("Enter the maximum number: ") 
             if not max_number.isdigit(): 
                 print("Invalid input! Please enter a valid number.") 
                 continue 
  
             attempts = input("Enter the number of attempts: ") 
             if not attempts.isdigit(): 
                 print("Invalid input! Please enter a valid number.") 
                 continue 
  
             min_number = int(min_number) 
             max_number = int(max_number) 
             attempts = int(attempts) 
             break 
  
         target_number = random.randint(min_number, max_number) 
  
         while attempts > 0: 
             while True: 
                 guess = input(f"Guess a number between {min_number} and {max_number}: ") 
                 if not guess.isdigit(): 
                     print("Invalid input! Please enter a valid number.") 
                     continue 
                 guess = int(guess) 
                 break 
  
             if guess == target_number: 
                 print("You won!") 
                 return 
  
             print("You lost! Try again.") 
             attempts -= 1 
  
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