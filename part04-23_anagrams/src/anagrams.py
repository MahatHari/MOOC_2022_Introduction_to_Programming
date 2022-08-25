# Write your solution here
def anagrams(str1, str2) -> bool:
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


if __name__ == "__main__":
    print(anagrams("tame", "meta"))  # True
    print(anagrams("tame", "mate"))  # True
    print(anagrams("tame", "team"))  # True
    print(anagrams("tabby", "batty"))  # False
    print(anagrams("python", "java"))  # False
