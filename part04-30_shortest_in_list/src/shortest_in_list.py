# Write your solution here
def shortest(list1: list) -> int:
    shortest = list1[0]
    for word in list1:
        if len(word) < len(shortest):
            shortest = word
    return (shortest)


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)
