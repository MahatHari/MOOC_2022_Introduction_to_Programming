# Write your solution here

def distinct_numbers(list1: list) -> list:
    result = []
    for i in sorted(list1):
        if i not in result:
            result.append(i)
    return result


if __name__ == "__main__":
    print(distinct_numbers([3, 2, 2, 1, 2, 3, 3, 1]))
