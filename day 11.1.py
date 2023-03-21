import random


def ace(u, c):
    if u == 'Ace':
        if u_sum >= 11:
            ua = 1
        else:
            ua = int(input('How would you like to interpret Ace as, 1 or 11?'))

    elif c == 'Ace':
        if c_sum >= 11:
            ca = 1
        else:
            ca = int(input('How would you like to interpret Ace as, 1 or 11?'))


def comp(us, cs):
    if us > 21:
        return f'Bust!\nYou Lost.'
    elif cs > 21:
        return 'You Won.'
    elif us > cs:
        return 'You Won!'
    elif cs > us:
        return 'You Lost!'
    else:
        return 'draw'



def deal(us,cs):
    user_cards.insert(len(user_cards), random.choice(cards))
    print(f'your: {user_cards} ')
    if cs < 18:
        com_cards.insert(len(com_cards), random.choice(cards))
        print(f'comp: [{com_cards[0]}, * ]')
    else:
        print(f'comp: [{com_cards[0]}, * ]')


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, ]
user_cards = [random.choice(cards), random.choice(cards)]
com_cards = [random.choice(cards), random.choice(cards)]
ace(user_cards, com_cards)
u_sum = int(user_cards[0])+int(user_cards[1])
c_sum = int(com_cards[0])+int(com_cards[1])
print(f'Your Cards: {user_cards} \nComputer Cards: [{com_cards[0]}]\nYour: {u_sum}\n')

conti = input('Deal? yes or no ')
while conti == 'yes':
    deal(u_sum, c_sum)
    c_sum += com_cards[len(com_cards)-1]
    u_sum += user_cards[len(user_cards)-1]
    if u_sum > 21 and c_sum > 21:
        print(f'\nyour cards: {user_cards} \nComputer: {com_cards} \nyour: {u_sum}, comp: {c_sum}')
        print('no one wins')
        exit()
    elif c_sum > 21:
        print(f'\nyour cards: {user_cards} \nComputer: {com_cards} \nyour: {u_sum}, comp: {c_sum}')
        print('You Won.')
        exit()
    elif u_sum > 21:
        print(f'\nyour cards: {user_cards} \nComputer: {com_cards} \nyour: {u_sum}, comp: {c_sum}')
        print(f'Bust!\nYou Lost.')
        exit()
    else:
        conti = input('Deal? yes or no ')


if c_sum < 15:
    com_cards.insert(len(com_cards), random.choice(cards))
    print(f'comp: [{com_cards[0]}, * ]')
    c_sum += com_cards[len(com_cards) - 1]
    comp(u_sum, c_sum)

comp(u_sum, c_sum)
print(f'\nyour cards: {user_cards} \nComputer: {com_cards} \nyour: {u_sum}, comp: {c_sum}')
