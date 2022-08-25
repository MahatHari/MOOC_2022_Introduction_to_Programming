# Write your solution here
import re


def first_word(sentence):
    index_of_space = sentence.find(" ")
    return sentence[0: index_of_space]


def second_word(sentence):
    word = sentence.split(" ")
    return word[1]


def last_word(sentence):
    word = sentence.split(" ")
    return word[-1]


# modal solution
def find_word(sentence, what):
    index = 0
    word = ""
    counter = 0
    while index < len(sentence):
        if sentence[index] == " ":
            counter += 1
            if counter == what:
                break
            word = ""
        else:
            word += sentence[index]
        index += 1
    return word


def first_word_v1(sentence):
    return find_word(sentence, 1)


def second_word_v1(sentence):
    return find_word(sentence, 2)


def third_word_v1(sentence):
    return find_word(sentence, 0)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
