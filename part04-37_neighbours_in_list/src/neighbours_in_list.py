# Write your solution here

def longest_series_of_neighbours(list1: list) -> int:
    longest = 1
    result = 1
    for i in range(1, len(list1)):

        if abs(list1[i-1]-list1[i]) == 1:
            result += 1
        else:
            result = 1
        longest = max(longest, result)
    return longest


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
