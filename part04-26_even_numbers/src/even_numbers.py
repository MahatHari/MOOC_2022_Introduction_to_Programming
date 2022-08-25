# Write your solution here
def even_numbers(list1: list) -> list:
    result = []
    for i in list1:
        if i % 2 == 0:
            result.append(i)
    return result


if __name__ == "__main__":
    print(even_numbers([1, 2, 3, 4, 5]))
