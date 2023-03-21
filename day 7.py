#hangman game

import random
import words
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
#words = ['rabbits', 'vacancy', 'ukelele']
print(logo)
random_word = random.choice(words.word_list)
print(random_word)

dash = '_'*len(random_word)
dashs = list(dash)

lives = 7
while dashs != '_':
    guess = input('guess a letter: ').lower()
    if guess in dashs:
        print(f'you have already guessed {guess}')
    for pos in range(len(random_word)):
        letter = random_word[pos]

        if letter == guess:
            dashs[pos] = letter

    if guess not in random_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print(f'you lost \nThe word was: {random_word}')
            exit()

    final_word = ''.join(dashs)
    print(final_word)

    if final_word == random_word:
        print('you won')
        exit()

