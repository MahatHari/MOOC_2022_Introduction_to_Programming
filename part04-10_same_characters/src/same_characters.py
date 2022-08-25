# Write your solution here
from operator import truediv


def same_chars(text, index1, index2):
    last_index = len(text)-1
    if index1 > last_index or index2 > last_index:
        return False
    elif text[index1] == text[index2]:
        return True
    else:
        return False


# model Solution
def sam_chars_v2(string, a, b):
    if a >= len(string) or b >= len(string):
        return False
    return string[a] == string[b]


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("coder", 1, 5))
