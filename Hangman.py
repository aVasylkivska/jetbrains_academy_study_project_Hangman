import random

words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
first_try = input('''H A N G M A N
Guess the word: ''')

if first_try == word:
    print('You survived!')
else:
    print('You are hanged!')
