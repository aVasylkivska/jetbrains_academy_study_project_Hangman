import random

words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)

print('H A N G M A N\nGuess the word {}{}:'.format(word[0:3], '-' * (len(word) - 3)))
first_try = input()

if first_try == word:
    print('You survived!')
else:
    print('You are hanged!')
