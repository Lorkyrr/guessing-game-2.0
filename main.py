import random

def guess_the_number():

    secret_number = random.randint(1, 100)

    tries = 10
    print("Welcome to the guessing game! Guess the secret number from 1 to 100. You have 10 attempts!")

    # Loop that continues while there are still attempts left
    while tries > 0:
        print(f"\nYou have {tries} attempts remaining.")
        prediction = int(input("Enter your guess: "))

    # Verifies if the guess is correct, too low, or too high
        if prediction == secret_number:
            print("Congratulations! You guessed the secret number!")
            break
        
        elif prediction < secret_number:
            print("Your guess is too low. Try again!")
        
        else:
            print("Your guess is too high. Try again!")
    
    # Reduz o número de tentativas
        tries -= 1

    else:
        print(f"\nUnfortunately, you're out of attempts! The secret number was {secret_number}.")

# Inicia o jogo
guess_the_number()