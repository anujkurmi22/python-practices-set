'''WAP to get sum , differance , product of two numbers '''
def add():
    num1 = int(input("enter 1st number : "))
    num2 = int(input("enter 2nd number : "))
    total_sum = num1 + num2
    difference = num1 - num2 
    product = num1 * num2

    print("sum:" , total_sum)
    print("diffrence: ", difference)
    print("product: ", product)
add()
