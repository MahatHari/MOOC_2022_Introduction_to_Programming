# Name and Age
# sample out put
# What is your name? Frances Fictitious
# Which year were you born? 1990
# Hi Frances Fictitious, you will be 31 years old at the end of the year 2021


name = input("What is your name?")
dob = int(input("Which year were you born?"))
print(f"Hi {name}, you will be {2021-dob} years old at the end of the year 2021")


# Fix the code: Product

number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number1 * number2 * number3

print("The product is", product)

# sum and product
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
print(f"The sum of the numbers: {num1+num2}")
print(f"The product of the numbers: {num1*num2}")

# Food expenditure

times = int(input("How many times a week do you eat at the student cafeteria"))
price = float(input("The price of a typical student lunch?"))
grocery = float(input("How much money do you spend on groceries in a week?"))
total_lunch = times*price
total = total_lunch+grocery
perday = total/7

print(f"Average food expenditure:")
print(f"Daily: {perday} euros")
print(f"Weekly: {total} euros")

#Strudents in group
student = int(input("How many students on the course?"))
size = int(input("Desired group size? "))

if student % size > 0:
    groups = student//size + 1
else:
    groups = student//size

print(f"Number of groups formed: {groups}")
