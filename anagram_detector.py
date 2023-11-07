# Write a function that determines if two words are anagrams of each other.
# An anagram is a word or phrase formed by rearranging the letters of another.

import random

word_1 = 'abbac'
word_2 = 'baabca'


def checker_random(w1, w2):
    for i in range(0, 10000):
        w2_random = ''.join(random.sample(w2, len(w2)))
        if w1 == w2_random:
            print(w1 + ' ' + w2_random)
            print('success')
            break


def checker(w1, w2):

    word_1_list = list(w1)
    word_2_list = list(w2)

    if len(w1) == len(w2):
        for letter in word_1_list:
            try:
                # .remove removes the first letter in this case
                word_2_list.remove(letter)
            except ValueError:
                pass
            print(word_2_list)
    else:
        print(w1 + ' is not an anagram of ' + w2)
        quit()

    if len(word_2_list) == 0:
        print(w1 + ' is an anagram of ' + w2)
    else:
        print(w1 + ' is not an anagram of ' + w2)


checker(word_1, word_2)
