#cipher version1

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
d = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
t = input("Type your message:\n").lower()
s = int(input("Type the shift number:\n"))
c = ''

def encrypt():
    nt = list(t)
    global c
    c = ''

    for letter in nt:
        pos = a.index(letter) + s

        if pos >= 27:
            pos = (pos-26)

        n = a[pos]
        c += n
    print(c)



def decrypt():

    z = list(c)
    d = ''

    for le in c:
        po = a.index(le) - s
        if po < 0:
            po = po + 26
        m = a[po]
        d += m
    print(d)

while True:
    if d == 'encode':
        encrypt()
        d = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    else:
        decrypt()
        d = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()





#cipher version2

import words
print(words.logo)


def caesar(st, sf, dr):
    et = ''
    if dr == 'decode':
        sf *= -1

    for char in st:
        if char in a:
            pos = a.index(char)
            np = pos + sf
            et += a[np]
        else:
            et += char

    print(f'the {dr}d text is: {et}')


is_true = True
while is_true:

    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    d = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    t = input("Type your message:\n").lower()
    s = int(input("Type the shift number:\n"))

    if s > 27:
        s = s % 26

    caesar(st=t, sf=s, dr=d)

    yn = input('should we continue? ').lower()
    if yn == 'no':
        print('goodbye')
        is_true = False
    else:
        is_true = True

