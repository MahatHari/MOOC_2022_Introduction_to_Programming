# Write your solution here
from this import d


a_list = []
while True:
    print(f"The list is now {a_list}")
    choice = (input("a(d)d, (r)emove or e(x)it"))
    if choice == "d":
        add = len(a_list)+1
        a_list.append(add)
    if choice == "r" and len(a_list) > 0:
        rmv = len(a_list)
        a_list.remove(rmv)
    if choice == "x":
        print("Bye!")
        break
