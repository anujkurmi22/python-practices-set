# Program to find the largest of three numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

print("The largest number is", largest)
