# The Memory game

import time
import os
import random

print("\t\t\t\tWe are going to play a memory game\n\n")
print('''You will be given a group of word to memorise 
         which will be cleared after 10 seconds and you will 
         have to type them out in the same other
         have fun''')

word_list = ["apple","pencil","toyota","crayon","peter","water","juice","school","lion","river"]
# create a function that picks random words from the list_name
def chose_words():
    the_words = []
    while len(the_words) < 4:
        the_words.append(random.choice(word_list)) 
    return the_words

print("memorise this words which would be cleared in 10 seconds\n\n")
sel_words = chose_words()
print(sel_words)

time.sleep(10)
os.system('cls')

your_answer = []
first_word = input("Enter the first word: ")
your_answer.append(first_word)
second_word = input("Enter the second word: ")
your_answer.append(second_word)
third_word = input("Enter the third word: ")
your_answer.append(third_word)
forth_word = input("Enter the forth word: ")
your_answer.append(forth_word)

if your_answer == sel_words:
    print("You have a nice memory")
else:
    print("You have a mild memory")