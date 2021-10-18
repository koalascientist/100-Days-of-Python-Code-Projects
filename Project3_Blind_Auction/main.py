from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program")

auction_dictionary = {}

continue_auction = True

while continue_auction:
  name = input("What is your name?\n")
  bid = int(input("What is your bid?\n$"))
  auction_dictionary[name] = bid
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
  if other_bidders == "yes":
    clear()
  else:
    continue_auction = False

winners = []
max_bid = 0
for key in auction_dictionary:
  key_value = auction_dictionary[key]
  if key_value > max_bid:
    max_bid = key_value
    winners = [key]
    ending = " is"
  elif key_value == max_bid:
    winners.append(key)
    ending = "s are"
winners_string = " and ".join(winners)
  
print(f"The winner{ending} {winners_string} with a bid of ${max_bid}.")




