# Write your solution here
a_list = [1, 2, 3, 4, 5]

index = int(input("Index: "))
while index != -1:
    new_val = int((input("New value: ")))
    a_list[index] = new_val
    print(a_list)
    index = int(input("Index: "))
