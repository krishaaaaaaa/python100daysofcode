import words
print(words.logo1)
print('Welcome to Silent Auction')
c = 'yes'
data = {}
conti = True

def comp(dat):
    hm = 0
    w = ''
    for ke in dat:
        amt = dat[ke]
        if amt > hm:
            hm = amt
            w = ke
    print(f'highest bidder is {w} and the bidding was {hm}')


while conti:

    a = input('what is you name? ')
    b = int(input('how much is you bid? '))

    data[a] = b
    c = input('are there any more bidders? enter yes or no ')
    if c == 'no':
        comp(data)
        conti = False
