# you have to choose a random english word from a list.
# you have 6 chanches to guess it.
# every time when you make a wrong guess, your chanches will be reduced 

import random
from words import wordList
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses a word from the given list
    while '_' in word or ' ' in word:
        word = random.choice(words) # if the selected word contains '_' or ' ' then select a new word

    return word.upper()

def hangman():     
    word = get_valid_word(wordList)
    word_letters_set = set(word) #letters in the word as a set. it have only unique characters
    # print(word_letters_set)
    alphabet_set = set(string.ascii_uppercase) # getting all the letters in the english alphabet
    # print(alphabet_set)
    used_letters_set = set() # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters_set) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters_set))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters_set else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))


        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet_set - used_letters_set:
            used_letters_set.add(user_letter)
            if user_letter in word_letters_set:
                word_letters_set.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in word.')     

        elif user_letter in used_letters_set:
            print('You have already used that character. Please try again!')

        else:
            print('Invalid character. Please try again.')    

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was ', word)
    else:
        print('Congratulations!!. You guessed the word ', word, ' correctly.')


hangman()