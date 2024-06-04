import random

# Set the secret number
secret_number = random.randint(1, 10)  # Change 10 to adjust the guess range

# Welcome message
print("Welcome to the guessing game!")

# Initialize guesses
guesses = 0

# Main game loop
while True:
  # Get user's guess
  try:
    guess = int(input("Guess a number between 1 and 10: "))
  except ValueError:
    print("Please enter a valid number.")
    continue
  guesses += 1

  # Check the guess
  if guess == secret_number:
    print(f"You guessed it in {guesses} tries! Congratulations!")
    break
  elif guess < secret_number:
    print("Your guess is too low. Try again!")
  else:
    print("Your guess is too high. Try again!")

# End message
print("Thanks for playing!")
