# Write your solution here

def histogram(string: str) -> dict:
    char_occurance = {}

    for char in string:
        if char not in char_occurance:
            char_occurance[char] = 0
        char_occurance[char] += 1

    for key, value in char_occurance.items():
        print(f"{key} {'*'*value}")


if __name__ == "__main__":
    histogram("statistically")
