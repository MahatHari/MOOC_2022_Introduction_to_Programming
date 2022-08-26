# Write your solution here


def create_update_phonebook(phone_book: dict, string: str, phonenumber: str) -> dict:
    phone_book[string] = phonenumber


def search_phonebook(phone_book: dict, string: str) -> str:
    if string in phone_book:
        return phone_book[string]
    else:
        return "no number"


def main():
    phone_book = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 1:
            name = input("name: ")
            found = search_phonebook(phone_book, name)
            print(found)
        if command == 2:
            name = input("name: ")
            number = input("number: ")
            create_update_phonebook(phone_book, name, number)
            print("ok!")
        if command == 3:
            print("quitting...")
            break


main()
