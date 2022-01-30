import art
from game_data import data
import random
from replit import clear

def get_person_info(input_list, position, guess_order):
  """" Print the information of the person/object given the order number, guess order, and the list of dictionaries that contains the input information """
  name = input_list[position]["name"]
  description = input_list[position]["description"]
  country = input_list[position]["country"]
  if guess_order == "A":
    start_string = "Compare"
  else: 
    start_string = "Against"
  print(f"{start_string} {guess_order}: {name}, a {description}, from {country}")

def compare_followers(input_list, option_A_index, option_B_index):
  """ Returns the option that has the highest number of followers. """
  if input_list[option_A_index]["follower_count"] > input_list[option_B_index]["follower_count"]:
    return option_A_index
  elif input_list[option_A_index]["follower_count"] == input_list[option_B_index]["follower_count"]:
    return 999999
  else:
    return option_B_index

# Print game logo
print(art.logo)

# Create a variable that will count the score
score = 0

# Game flag
continue_game = True

# Generate random number between 0 and len(data)
guesses = random.sample(range(0,len(data)), k = 2)
guesses_dict = {"A": guesses[0], "B": guesses[1]}

while continue_game:

  # If the game continues, for the next round, get option B as option A, and generate a new option.
  if score > 0:
    guesses_dict["A"] = guesses_dict["B"]
    new_guess_index = random.randint(0, len(data)-1)
    while guesses_dict["A"] == new_guess_index:
      new_guess_index = random.randint(0, len(data)-1)
    guesses_dict["B"] = new_guess_index

  get_person_info(data, guesses_dict["A"], "A")

  # Print vs logo
  print(art.vs)

  get_person_info(data, guesses_dict["B"], "B")
  choice = input("Who has more followers? Type 'A' or 'B': ").upper()


  # Get the index of the winner
  winner_position = compare_followers(data, guesses_dict["A"], guesses_dict["B"])

  clear()

  # Print game logo
  print(art.logo)

  # Check if user guessed correctly
  if winner_position == 9999999:
    print("It's a draw. No additional points are given. The game continues.")
  elif winner_position == guesses_dict[choice]:
    score += 1
    print(f"You're right! Current score: {score}.")
  else: 
    print(f"Game over. Your total score is {score}.")
    continue_game = False

