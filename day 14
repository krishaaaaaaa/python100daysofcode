#Higer or Lower Game

import random
import words


def comp(ch, p):
    e = int(a[0]['follower_count'])
    d = int(a[1]['follower_count'])
    if ch == 'A' and e > d:
        return f'Score: {p}'
    elif ch == 'A' and d > e:
        print('You Lose')
        exit()
    elif ch == 'B' and e > d:
        print('You Lose')
        exit()
    elif ch == 'B' and d > e:
        return f'Score: {p}'
    else:
        print('Invalid')
        exit()


points = 1

a = random.sample(words.data, 2)
print(f"Compare A: {a[0]['name']}, a {a[0]['description']}, from {a[0]['country']}\n\n\nCompare B: {a[1]['name']}, a {a[1]['description']}, from {a[1]['country']}\n")
choice = input('Who do you think has more followers A or B? ').upper()
res = comp(choice, points)
print(res)


while points < 5:
    points += 1
    e = int(a[0]['follower_count'])
    d = int(a[1]['follower_count'])

    if e > d:
        a = [a[0], random.choice(words.data)]
        if a[0] == a[1]:
            a[1] = random.choice(words.data)
    else:
        a = [a[1], random.choice(words.data)]
        if a[0] == a[1]:
            a[0] = random.choice(words.data)

    print(f"Compare A: {a[0]['name']}, a {a[0]['description']}, from {a[0]['country']}\n\n\nCompare B: {a[1]['name']}, a {a[1]['description']}, from {a[1]['country']}\n")
    choice = input('Who do you think has more followers A or B? ').upper()
    res = comp(choice, points)
    print(res)
print(f'You final Score is: {points}')
