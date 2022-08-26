# Write your solution here
def dict_of_numbers():
    dictionary = {}
    num_to_words = {0: "zero", 1: "one", 2: "two", 3: "three",
                    4: "four", 5: "five", 6: "six", 7: "seven",
                    8: "eight", 9: "nine", 10: "ten", 11: "eleven",
                    12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
                    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
                    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
                    60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
    for num in range(0, 100):
        if num in num_to_words:
            dictionary[num] = num_to_words[num]
        else:
            t = (num//10) * 10
            r = num % 10
            dictionary[num] = num_to_words[t]+"-"+num_to_words[r]
    return dictionary

# modal solution:


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers)
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
