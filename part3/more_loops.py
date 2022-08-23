# Multiplications

num = int(input("Please type in a number:"))

for i in range(1, num+1):
    for j in range(1, num+1):
        print(f"{i} x {j} = {i*j} ")


# first letter in word

sentence = input("Please type in a sentence")

words = sentence.split(" ")
for word in words:
    print(word[0])

# model solution for first letter in word

sentence = " "+sentence
index = 1
while index < len(sentence):
    if sentence[index-1] == " " and sentence[index+1] != " ":
        print(sentence[index])
    index += 1


# Factorial

f_num = int(input("Please type in a number: "))
while f_num > 0:
    n = 1
    factorial = 1
    while n != 1:
        factorial *= n
        n += 1
    print(f"The factorial of the number {num} is {factorial}")
    num = int(input("Please type in a number"))
print("Thanks and")


# Flip the pairs
# Please write a program which asks the user to type in a number.
# The program then prints out all the positive integer values from 1 up to the number.
#  However, the order of the numbers is changed so that each pair or numbers is flipped.
#   That is, 2 comes before 1, 4 before 3 and so forth.

num = int(input("Please type in a number "))
i = 1
while i <= num:
    if i+1 <= num:
        print(i+1)
    print(i)
    i += 2


#  Taking turns

# Please write a program which asks the user to type in a number.
# The program then prints out the positive integers
# between 1 and the number itself, alternating between the two ends of the range as in the examples below.

num = int(input("Please type in a number: "))

left = 1
right = num

while left < right:
    print(left)
    print(right)
    left += 1
    right -= 1
if left == right:
    print(left)
