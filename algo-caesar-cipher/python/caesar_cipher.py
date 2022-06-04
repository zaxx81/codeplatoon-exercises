def caesar_cipher(string, shift_amount):
  # alpha_upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  # alpha_lower = list('abcdefghijklmnopqrstuvwxyz')
  # print(alpha_upper[0])
  result = ""

  for char in string:
    if (char.isupper()):
      result += chr((ord(char) + shift_amount-65) % 26 + 65)
    elif (char.islower()):
      result += chr((ord(char) + shift_amount-97) % 26 + 97)
    else:
      result += char
  
  return result
