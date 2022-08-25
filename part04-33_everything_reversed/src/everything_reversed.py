# Write your solution here

def everything_reversed(my_list: list) -> list:
    result = []
    for word in my_list:
        result.append(word[::-1])
    return result[::-1]


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
