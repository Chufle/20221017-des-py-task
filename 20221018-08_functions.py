# write a function that prints out if the the division of two numbers has a remainder

from signal import pause


def has_remainder(number_one,number_two):
    out = number_one % number_two
    print(out)

has_remainder(10,2)

print("#######################")
#write a function that returns a given string in reverse order

def encrypt(word_one):
    word_two = ""
    for letter in word_one:
        word_two = letter + word_two
    return word_two

print(encrypt("Europa"))

#write a function that takes a string and returns the snakecase version of this string
# Example: This is a file => this_is_a_file

def snakecaser(sentence):
    #for letter in sentence:
    out=""
    #lower_sentence = sentence.lower()
    for letter in sentence:
        if letter == " ":
            out = out + str("_")
        elif letter.isupper() == True:
            print(letter)
            print(letter.isupper())
            out == out + str(letter.lower())
        else:
            out = out + str(letter)
    print(out)

snakecaser("Hey das ist ein tollesProgramm")

import stringcase
print(stringcase.snakecase('FooBarBaz'))