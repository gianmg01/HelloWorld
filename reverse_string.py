
word = str(raw_input("enter a word  "))
new_word = ""
counter = len(word) - 1

for x in word:
    new_word += word[counter]
    counter -= 1

print("the word you entered backwards is:  ", new_word)