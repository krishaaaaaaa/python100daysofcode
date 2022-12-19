import random


def comp(g, rn, it):
    if g == rn:
        print(f'You got it! The answer is :{g}')
        exit()
    elif g > rn:
        print(f'Too High!\nGuess Again')
    elif g < rn:
        print(f'Too Low!\nGuess Again')


print(f'Welcome to Number Guessing Game! \nI am thinking of a number between 1 to 100')
random_num = random.randrange(1, 101)
print(random_num)

level = input("Choose a Difficulty level, type 'easy' or 'hard' : ")
if level == 'easy':
    chance = 10
elif level == 'hard':
    chance = 5
else:
    print('Invalid choice of difficulty')
    chance = 0
    exit()
print(f'You have {chance} attempts to guess the right number.')

is_true = True
while is_true:
    guess = int(input('Make a Guess: '))
    comp(guess,random_num,is_true)
    chance -= 1
    print(f'\nYou have {chance} attempts lefts')
    if chance == 0:
        print(f'The answer was: {random_num} \nYou Lose :( ')
        is_true = False

