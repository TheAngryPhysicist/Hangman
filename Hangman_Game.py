from Hangman import HangmanGame
import random
import requests

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
words = response.text.splitlines()

flag = 0
while True:
    if flag == 0:
        word = random.choice(words)
        HangmanGame(word).game_loop()
        answer = input("Would you like to continue? y-yes n-no  :")
        if answer == 'y':
            flag = 0
            continue
        elif answer == 'n':
            break
        else:
            print('You must enter either a y or n!')
            flag = 1
    else:
        answer = input("Would you like to continue? y-yes n-no  :")
        if answer == 'y':
            flag = 0
            continue
        elif answer == 'n':
            break
        else:
            print('You must enter either a y or n!')
            flag = 1
