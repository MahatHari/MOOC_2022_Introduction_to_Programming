# Write your solution here
def add(phone_book: dict):
    name = input("name: ")
    number = input("number: ")
    if name not in phone_book:
        phone_book[name] = []
    (phone_book[name]).append(number)
    print("ok!")


def search(phone_book: dict):
    name = input("name: ")
    if name in phone_book:
        for phonenumber in phone_book[name]:
            print(phonenumber)
    else:
        print("no number")


def main():
    phone_book = {}
    while True:
        command = int(input("command(1 search, 2 add, 3 quit): "))
        if command == 1:
            search(phone_book)
        if command == 2:
            add(phone_book)
        if command == 3:
            print("quitting...")
            break


main()
