# Write your solution here
list_size = int(input("How many items: "))
a_list = []
i = 0
while i < list_size:
    val = int(input(f"Item {i+1}:"))
    a_list.append(val)
    i += 1

print(a_list)
