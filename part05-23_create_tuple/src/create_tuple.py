# Write your solution here
from cgitb import small


def create_tuple(x: int, y: int, z: int) -> tuple:
    lst = [x, y, z]
    smallest = min(lst)
    greatest = max(lst)
    all = sum(lst)
    return (smallest, greatest, all)


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
