import random

def guess_number():
    target_number = random.randint(1, 10)
        attempts = 0

            while True:
                    guess = int(input("Guess a number between 1 and 10: "))
                            attempts += 1

                                    if guess == target_number:
                                                print("You won!")
                                                            break
                                                                    else:
                                                                                print("You lost! Try again.")

                                                                                        if attempts >= 3:
                                                                                                    print("You have reached the maximum number of attempts.")
                                                                                                                print("The target number was", target_number)
                                                                                                                            break

                                                                                                                            guess_number()