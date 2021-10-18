alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar (message, shift_amount, direction):
  execute_flag = True

  if direction not in (["encode","decode"]):
    print("You entered the wrong direction.")
    execute_flag = False

  if shift_amount > 26:
    shift_amount %= 26

  if execute_flag:
    final_text = ""
    for letter in message:
      if letter not in alphabet:
        final_text += letter
      else:
        current_index = alphabet.index(letter)
        if direction == "encode":
          if current_index + shift_amount >= len(alphabet):
            new_index = current_index + shift_amount - len(alphabet)
          else:
            new_index = current_index + shift_amount
        else:
          new_index = current_index - shift_amount
        final_text += alphabet[new_index]
    print(f"The {direction}d text is {final_text}.")

from art import logo

print(logo)

answer = "yes"

while answer == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(message=text, shift_amount=shift, direction=direction)

  answer = input("Do you want to restart the cypher?\n").lower()
