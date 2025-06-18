

letters_tn = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
numbers_tl = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
input_message = []
numbered_input = []

user_input = input("what would you like to decryp? ")

for letter in user_input : 
    if letter.lower() in letters_tn :
        numbered_input.append(letters_tn[letter.lower()])
    else :
        numbered_input.append(letter)

print(numbered_input)

num_freq = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0}
for num in numbered_input :
    if num in num_freq :
        num_freq[num] = num_freq[num] + 1

print(num_freq)
# the list is sorted by highest frequency
sorted_num_freq = sorted(num_freq, key=num_freq.get, reverse=True)

print(sorted_num_freq[0])

rank_to_letter = {
    0: 'e', 1: 't', 2: 'a', 3: 'o', 4: 'i', 5: 'n', 6: 's', 7: 'h', 8: 'r', 9: 'd', 10: 'l', 11: 'c', 12: 'u', 13: 'm', 14: 'w', 15: 'f', 16: 'g', 17: 'y', 18: 'p', 19: 'b', 20: 'v', 21: 'k', 22: 'j', 23: 'x', 24: 'q', 25: 'z'}


# do a for loop that uses the highest frequency number and goes though the rank_to_letter to recreate the scentence then maybe have something check if the work is a real word
for num in sorted_num_freq : 
    