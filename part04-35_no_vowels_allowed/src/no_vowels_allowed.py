# Write your solution here
def no_vowels(string: str) -> str:
    vowels = "aeiou"
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    return result


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
