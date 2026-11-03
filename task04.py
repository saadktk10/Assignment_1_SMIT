#Number Guessing Game

def check_guess(guess, secret):
    if guess == secret:
        return "Correct!"
    elif guess < secret:
        return "Too low!"
    else:
        return "Too high!"

secret_number = 7
attempts = 0
player_name = input("Enter your name: ")
score = 0

while attempts < 5:
    try:
        guess = int(input("Guess the number (1-10): "))
        attempts += 1
        
        result = check_guess(guess, secret_number)
        print(result)
        
        if result == "Correct!":
            score = 6 - attempts  # Higher score for fewer attempts
            print(f"You won in {attempts} attempt(s)!")
            break
    except ValueError:
        print("Please enter a valid integer.")

if attempts == 5 and result != "Correct!":
    print(f"Game over! The secret number was {secret_number}.")

# Challenge: Store the player's name and score in a dictionary
player_record = {
    "name": player_name,
    "score": score,
    "attempts": attempts
}

print("\nPlayer Record:", player_record)