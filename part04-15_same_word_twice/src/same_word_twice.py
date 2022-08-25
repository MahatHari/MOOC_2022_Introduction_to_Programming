# Write your solution here

a_list = []

while True:
    word = input("Word: ")
    if word in a_list:
        size = len(a_list)
        print(f"You typed in {size} different words")
        break
    else:
        a_list.append(word)
