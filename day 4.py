#rock, paper, scissors game
import random
pi = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if pi > 2:
    print('invalid input')
else:
    p = ['rock', 'paper', 'scissors']
    c = random.choice(p)
    p1 = p[pi]
    print(f'player: {p1} \ncomputer: {c}')

    if p1 == 'rock' and c == 'paper':
        print("Computer Won!")
    elif p1 == 'rock' and c == 'scissors':
        print('Player Won!')
    elif p1 == 'paper' and c == 'rock':
        print('Player Won!')
    elif p1 == 'paper' and c == ' scissors':
        print("Computer Won!")
    elif p1 == 'scissors' and c == 'rock':
        print("Computer Won!")
    elif p1 == 'scissors' and c == 'paper':
        print('Player Won!')
    else:
        print('Draw Match')



