# Write your solution here

a_list = []
while True:
    item = int(input("New item: "))
    if item == 0:
        break
    else:
        a_list.append(item)
        print(f"The list now: {a_list}")
        print(f"The list in order: {sorted(a_list)}")
print("Bye!")
