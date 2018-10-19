from __future__ import print_function
from random import randint


game = 1
match = 1
words = ("die hard",
         "shawshank redemption",
         "top gun",
         "john wick",
         "pulp fiction",
         "avengers: infinity war",
         "mad max: fury road",
         "casino royale",
         "pirates of the caribbean: the curse of the black pearl",
         "harry potter and the chamber of secrets")
letters_guessed = ""
letters_remain = ["a","b","c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letters_remain_2 = ""
word_picked = ""
dash_word = ""
dash_word_checker = ""
guess = ""
guesses_left = 6


while game == 1:

    word_picked = words[randint(0, 9)]

    counter = 0

    for x in word_picked:

        if word_picked[counter] != ' ' and word_picked[counter] != ':':
            dash_word += '-'
        else:
            dash_word += word_picked[counter]
        counter += 1

    while match == 1:

        print ("=====================================================================================================")
        print (dash_word)
        letters_remain_2 = ""
        for x in letters_remain:
            letters_remain_2 += x
        print ('letters remaining:  ', letters_remain_2)
        print ('letters guessed:  ', letters_guessed)
        print ('you have ', guesses_left, ' guesses left')
        print ("=====================================================================================================")
        guess = str(raw_input("enter a letter:  "))

        counter2 = 0

        for x in dash_word:

            if word_picked[counter2] == guess:

                dash_word_checker += guess

            else:
                dash_word_checker += dash_word[counter2]

            if dash_word_checker == dash_word:
                guesses_left -= 1

            counter2 += 1

        letters_remain.remove(guess)
        letters_guessed += guess
        dash_word = dash_word_checker
        dash_word_checker = ""
        counter2 = 0

        if guesses_left == 0 or dash_word == word_picked:
            break

    if guess == 0:

        print ("game over! would you like to try again? (y/n)")
        play_again = str(raw_input(""))

        if play_again == "n":
            break
    elif guess > 0:
        print ("You got the word! would you like to try again? (y/n)")
        play_again = str(raw_input(""))

        if play_again == "n":
            break

    letters_guessed = ""
    letters_remain = "abcdefghijklmnopqrstuvwxyz"
    word_picked = ""
    dash_word = ""
    dash_word_checker = ""
    guess = ""
    guesses_left = 6

print("Thanks for playing, have a nice day!!! :)")