# Write your solution here
def length_of_longest(list1: list) -> int:
    longest = list1[0]
    for word in list1:
        if len(word) > len(longest):
            longest = word
    return len(longest)


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)
