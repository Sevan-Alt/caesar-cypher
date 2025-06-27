letters = 'abcdefghijklmnopqrstuvwxyz'

user_input = input("what would you like to decrypt? ")
encoded = []
frequency = []
removed_characters = {}
point = 0

for letter in user_input:
    if letter in letters :
        encoded.append(letters.index(letter.lower()))
        point += 1
    elif letter not in removed_characters:
        removed_characters[letter] = user_input.index(letter)
    else :
        removed_characters[letter]


print(encoded)

for num in range(len(encoded)) : 
    encoded[num] += 1
print(encoded)
print(removed_characters)