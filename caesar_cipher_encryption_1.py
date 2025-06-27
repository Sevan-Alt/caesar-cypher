import random

user_input = input("what is your message? ")
letters = 'abcdefghijklmnopqrstuvwxyz'
encrypted = ''
random_number = random.randrange(1,26)

for letter in user_input:
    if letter in letters :
        encrypted += letters[((letters.index(letter.lower()))+random_number)%26]
    else :
        encrypted += letter
print(encrypted)

