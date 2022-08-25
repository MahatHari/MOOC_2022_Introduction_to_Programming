# Write your solution here
def spruce(size):
    print("a spruce!")
    i = 1
    spaces = 0
    while i <= size:
        spaces = (size-i)//2
        print(" "*spaces+"*"*i+" "*spaces)
        i += 2
    print(" "*(size//2)+"*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(99)
