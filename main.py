def print_menu():
    print("What do you want to play?")
    print("[1] Guess the number")
    print("[2] Think of a number")

def get_game_mode():
    while True:
        print_menu()
        game_mode = input("Type the game mode number: ")
        if game_mode in ['1', '2']:
            return game_mode
        print("Invalid input! Please choose 1 or 2.")

def play_game():
    game_mode = get_game_mode()
    if game_mode == '1':
        import guess_the_number
        guess_the_number.play_guess_user_number()
    else:
        import think_of_a_number
        think_of_a_number.play_think_of_a_number()

if __name__ == "__main__":
    play_game()
