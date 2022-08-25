# Write your solution here

def most_common_character(text: str) -> str:
    most = 0
    c = 0
    most_char = text[0]
    for char in text:
        c = text.count(char)
        if c > most:
            most = c
            most_char = char
    return most_char


# modal solution
def most_common_character_v1(text: str) -> str:
    most_common = text[0]
    for char in text:
        if text.count(char) > text.count(most_common):
            most_common = char
    return most_common


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
    first_string = "abcdbde"
    print(most_common_character_v1(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character_v1(second_string))
