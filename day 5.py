#Password Generator

import random
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
a = int(input(f'Welcome to Random Password Generator \nHow many letter? '))
b = int(input('How many numbers.: '))
c = int(input('How many special char: '))
p = (random.sample(l, a) + random.sample(n, b) + random.sample(s, c))

random.shuffle(p)

e = ' '
for f in p:
    h = str(f)
    e +=h
print(f'Your Password is:{e}' )
