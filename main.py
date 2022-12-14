from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

keep_playing = True

def ceasar(plain_text, shift_amount, direction_side):
    returned_text = ""
    if direction_side == 'decode':
      shift_amount *= -1
    for char in plain_text:
      if char in alphabet:
        position = alphabet.index(char)
        new_position = (position + shift_amount) % 26
        returned_text += alphabet[new_position]
      else:
        returned_text += char
    print(f"The {direction}d text is {returned_text}\n")

while keep_playing:
  # Get the input variables.
  direction = ""
  while direction not in ['encode', 'decode']:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # Run the function.
  ceasar(text, shift, direction)

  # Ask if the user wants to keep playing.
  keep_playing_input = input('Would you like to play again? Answer yes or no.\n')
  if keep_playing_input == 'no':
    keep_playing = False
    print('\nThe game has ended. See you next time :).')