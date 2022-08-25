# Write your solution here
def all_the_longest(list1: list) -> list:
    longest_list = []
    long = list1[0]
    for word in list1:
        if len(long) < len(word):
            long = word
    for word in list1:
        if len(word) == len(long):
            longest_list.append(word)
    return longest_list


# modal solution

def all_longest(names: list) -> list:
    result = []
    for name in names:
        if result == [] or len(name) > len(result[0]):
            result = [name]
        elif len(name) == len(result[0]):
            result.append(name)
    return result


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result)  # ['dorothy', 'richard']
