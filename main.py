import random

def difficulty_level():
    print("Select a difficulty level:")
    print("\n1. Easy (15 attempts)")
    print("2. Medium (10 attempts)")
    print("3. Hard (5 attempts)")
    print("4. Ultra Hard (3 attempts)")

    while True:
        choice = input("\nEnter your choice (1, 2, 3, or 4): ")

        try:
            choice = int(choice)
            if choice < 1 or choice > 4:
                raise ValueError
        except ValueError:
            print("\nInvalid input! Please enter a number between 1 and 4.")
            continue

        match choice:  
            case 1:
                return 15
            case 2:
                return 10
            case 3:
                return 5
            case 4:
                return 3
            case _:
                print("\nInvalid choice! Please select a valid difficulty level.")


def guess_the_number():

    secret_number = random.randint(1, 100)

    tries = difficulty_level()

    # Prediction history and dynamic limits for tips
    previous_guesses = []
    lower_limit = 1
    upper_limit = 100

    print(f"\nWelcome to the guessing game! Guess the secret number from 1 to 100. You have {tries} attempts!")

    # Loop that continues while there are still attempts left
    while tries > 0:
        print(f"\nYou have {tries} attempts remaining.")

        if previous_guesses:
            print(f"Previous guesses: {previous_guesses}")
            print(f"Current range: {lower_limit} to {upper_limit}")

        prediction = input("\nEnter your guess: ")

        # Validates if the input is an integer
        try:
            prediction = int(prediction)
        except ValueError:
            print("\nInvalid input! Please enter a valid integer.")
            continue

    # Validates if the input is within the specified range
        if prediction < 1 or prediction > 100:
            print("\nInvalid input! Please enter a number between 1 and 100.")
            continue

    # Check if the number has already been guessed
        if prediction in previous_guesses:
            print("\nYou've already guessed that number! Try a different one.")
            continue

        previous_guesses.append(prediction)
        
    # Verifies if the guess is correct, too low, or too high
        if prediction == secret_number:
            print("\nCongratulations! You guessed the secret number!")
            break
        
        elif prediction < secret_number:
            print("\nYour guess is too low. Try again!")
            if prediction >= lower_limit:
                lower_limit = prediction + 1
        
        else:
            print("\nYour guess is too high. Try again!")
            if prediction <= upper_limit:
                upper_limit = prediction - 1

    # Reduces the number of attempts
        tries -= 1

    else:
        print(f"\nUnfortunately, you're out of attempts! The secret number was {secret_number}.")

# Start the game
guess_the_number()