# Write your solution here

import re


def sum_of_positives(integers: list) -> int:
    sum = 0
    for i in integers:
        if i > 0:
            sum += i
    return sum


if __name__ == "__main__":
    result = sum([1, 2, -3, 4, 5, 6])
    print("The result is ", result)
