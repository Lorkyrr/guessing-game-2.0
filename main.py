import random

def guess_the_number():

    secret_number = random.randint(1, 100)

    tries = 10

    # Prediction history and dynamic limits for tips
    previous_guesses = []
    lower_limit = 1
    upper_limit = 100

    print("Welcome to the guessing game! Guess the secret number from 1 to 100. You have 10 attempts!")

    # Loop that continues while there are still attempts left
    while tries > 0:
        print(f"\nYou have {tries} attempts remaining.")

        if previous_guesses:
            print(f"Previous guesses: {previous_guesses}")
            print(f"Current range: {lower_limit} to {upper_limit}")

        prediction = (input("Enter your guess: "))

        # Validates if the input is an integer
        try:
            prediction = int(prediction)
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

    # Validates if the input is within the specified range
        if prediction < 1 or prediction > 100:
            print("Invalid input! Please enter a number between 1 and 100.")
            continue

    # Check if the number has already been guessed
        if prediction in previous_guesses:
            print("You've already guessed that number! Try a different one.")
            continue

        previous_guesses.append(prediction)
        
    # Verifies if the guess is correct, too low, or too high
        if prediction == secret_number:
            print("Congratulations! You guessed the secret number!")
            break
        
        elif prediction < secret_number:
            print("Your guess is too low. Try again!")
        
        else:
            print("Your guess is too high. Try again!")
    
    # Reduces the number of attempts
        tries -= 1

    else:
        print(f"\nUnfortunately, you're out of attempts! The secret number was {secret_number}.")

# Start the game
guess_the_number()