def generate_random():
  import random
  return random.randint(1,100)

def play_game(game_level): 
  continue_game = True

  if game_level == "easy":
    number_of_attempts = 10
  elif game_level == "hard":
    number_of_attempts = 5
  else:
    print("You entered an non-existent difficulty level")
    continue_game = False
  
  while continue_game:
    print(f"You have {number_of_attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == random_number:
      print(f"Congratulation! You guessed the number! The answer was {random_number}")
      continue_game = False
    elif guess > random_number:
      print("Too high. Guess again")
      number_of_attempts -= 1
    else:
      print("Too low. Guess again")
      number_of_attempts -= 1
    if number_of_attempts == 0:
      continue_game = False
      print(f"You've run out of guesses. You lose. The answer was {random_number}")


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()

# Generate random number
random_number = generate_random()


# Play the game
play_game(difficulty_level)
