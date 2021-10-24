import random

def draw_cards (no_cards):
  """Returns a list of random cards with length equal to no_cards"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  selected_cards = random.choices(cards, k = no_cards)
  return selected_cards

def check_ace_condition (l):
  """Checks if the score is over 21 and there are aces in the list. If this is the case, the ace will take value of 1."""
  if sum(l) > 21:
    l.remove(11)
    l.append(1)
  return l
  
def blackjack_game():

  continue_game = True
  show_result = False
  another_card = True

  game_start = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()

  if game_start == "n":
    continue_game = False

  while continue_game:
    your_cards = draw_cards(2)
    check_ace_condition(your_cards)
    computer_card = draw_cards(2)
   # print(computer_card)
    check_ace_condition(computer_card)
    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
    print(f"Computer's first card: {computer_card[0]}")
    
    if sum(your_cards) == 21 or sum(computer_card) == 21:
      show_result = True
      continue_game = False
    else:
      while another_card:
        another_card_decision = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card_decision == "y":
          your_cards += draw_cards(1)
          check_ace_condition(your_cards)
          if sum(your_cards)>=21:
            another_card = False
            show_result = True
            continue_game = False
          print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
          print(f"Computer's first card: {computer_card[0]}")
        else:
          another_card = False
          show_result = True
          continue_game = False

      while sum(computer_card)<17:
        computer_card += draw_cards(1)
        check_ace_condition(your_cards)

      show_result = True

  if show_result:  
    print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
    print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")

    if sum(your_cards) == 21 and sum(computer_card) == 21 and len(your_cards) == 2 and len(computer_card) == 2:
      print("It's a draw.")
    elif sum(your_cards) == 21 and len(your_cards) == 2 and len(computer_card) == 2:
      print("You got Blackjack. You win.")
    elif sum(computer_card) == 21 and len(your_cards) == 2 and len(computer_card) == 2:
      print("Computer got Blackjack. You lose.")
    elif sum(your_cards)>21:
      print("You went over. You lose.")
    elif sum(computer_card)>21:
      print("Computer went over. You win.")
    elif sum(your_cards) == sum(computer_card):
      print("It's a draw.")
    elif sum(your_cards) > sum(computer_card):
      print("You win.")
    else:
      print("You lose.")

    blackjack_game()


blackjack_game()
