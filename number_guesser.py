import random


def number_guesser():
    """This method runs the game based on the user's choice level"""
    from art import guess
    print("Welcome to the number guessing game!! \n")
    wanna_play = input("Would you like to guess a number? Type 'yes' or 'no' ").lower()
    if wanna_play == "yes":
        print(guess, "\n")
        print("I'm thinking of a number between 1 and 100 \n")

        def guess():
            number = random.randrange(101)
            return number

        game_over = False
        computer_guess = guess()

        level = input("Chose a difficulty level. Type 'e' for easy or 'h' for hard: ")
        if level == "e":
            print(f"\nYou have 10 attempts remaining to guess the number.")
            guess_count = 10
        elif level == "h":
            print(f"You have 5 attempts remaining to guess the number.")
            guess_count = 5

        while not game_over and guess_count != 0:
            user_guess = int(input("Make a guess: "))
            if user_guess == computer_guess:
                print("Congratulations! You guessed the correct number!")
                game_over = True
            else:
                if user_guess > computer_guess:
                    print("Too high!")
                    print("Guess again")
                elif user_guess < computer_guess:
                    print("Too low!")
                    print("Guess again")
                guess_count -= 1
                print(f"You have {guess_count} attempts remaining to guess the number.")
                print("---------------------------------------------------------------------------------------------")

    else:
        exit("Thanks for your interest! Goodbye........")


def run_again():
    """This method makes the game run again if the user wants to do so or exit if they don't"""
    play_again = input("Would you like to play again? Type 'yes' or 'no' ").lower()
    if play_again == "yes":
        number_guesser()
    else:
        exit("Goodbye........")


number_guesser()
run_again()
