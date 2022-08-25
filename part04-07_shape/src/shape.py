# Copy here code of line function from previous exercise and use it in your solution
def line(num, character):
    if character == "":
        character = "*"
    print(character*num)


def shape(num1, char1, num2, char2):
    for i in range(num1+1):
        line(i, char1)
    for i in range(num2):
        line(num1, char2)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
