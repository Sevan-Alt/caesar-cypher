import random

user_input = input("what is your message? ")
letters_tn = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
numbers_tl = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
numbered_input = []
for letter in user_input : 
    if letter in letters_tn :
        numbered_input.append(letters_tn[letter])
    else :
        numbered_input.append(letter)

print(numbered_input)
input_as_num = []

random_number = random.randrange(1,26)

for number in numbered_input :
    if isinstance(number, str) == False :
        input_as_num.append((number+random_number)%26)
    else :
        input_as_num.append(number)
print(input_as_num)

encrypted_input = []
for num in input_as_num:
    if num in numbers_tl :
        encrypted_input.append(numbers_tl[num])
    else :
        encrypted_input.append(num)
print(encrypted_input)