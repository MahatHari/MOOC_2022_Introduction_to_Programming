# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(word: str) -> bool:
    return word == word[::-1]


# model solution
def palindromes_v1(word: str) -> bool:
    for i in range(len(word/2)):
        if word[i] != word[len(word)-1]:
            return False
    return True


def main():
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")


main()
