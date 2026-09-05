'''
Function is a block of code
1. No return value and no argument
2. no return value but with argument
3. return value but  no argument 
4. return value but with argument
'''
# syntax
# def function_name(arg list):
#     Code
#     ''''''
#     ''''''
#     ''''''
#     return Value

# def show():                #signature
#     print('hello')         #function defination / body
#     print("I am show function")
#     print("Gullu beta ")

#     print()

# show()                      #function calling

# def anuj():
#    print("i am anuj kurmi")
#    print('i am from sagar')
#    print()
# anuj()

# print('__'* 20)

# a,b = 100,50
# print('additon:', a+b)
# print('subtraction:',a-b)
# print("multiplication :" ,a*b)
# print("division:",a//b)
# print("__"*20)

''' 2. No return value but with argument '''

# def calci(a,b):
#     print("addition:",a+b)
#     print("subtraction:", a-b)
#     print("multiplication:",a*b)
#     print("division:",a//b)
#     print('--'* 20)
# a,b = 1000 ,250
# calci(a,b)

# print("--"* 20)
# # calci(a:660,b:67)
# print(calci)
#  x, y = 8499, 499





# def wish(name,msg):
#     print('Hello MR.',name,'!',msg ,"age","22")
# wish('Anuj','you are  Software Developer.....')
# # print("_*_")

""" 3 Return value but no argument"""

# def count():
#     age=18
# print(count())



# c= count()
# print(count)


def factorial(n):
    fa=1
    for i in range (1,n+1):
        fa*1
print(factorial(5))


def getAge(birthAge):
    return 2026-birthAge
print("your age is :" , getAge(2004))

def info (name,age,address):
    return name is "Anuj Kurmi ",age is" 22" ,address is "vijay nagar indore "
print()


def getAge(birthAge):
    return 2026-birthAge
print("you Age is :", getAge(2004))


# def number(a,b):
#     sum_result= a+b
#     return sum_result
# total= number(10,29)
# print("The total is " ,total)

# function returning multiple value

# def  calci(a,b):
#     return a+b ,b-a ,a*b ,a/b

# print(calci(20,50))
# tt = calsi(20 , 50)
# print(tt)
# print(tt[0])
# print(tt[1])
# print(tt[2])
# print(tt[3])


# def  squre(n):
#     return n*n
# x=8
# print(squre(x))
# print("--" * 20)




'''take a list from the user and print its sum of all value in list '''

# def sumAll(grp):
#     s = 0
#     for i in (grp):
#         s += i
#     return s
# li = [11,12,13,14,175]
# print(sumAll(li))


#type of parameterized / Argument
#positional parameter
# Default parameter
# keyword argument
# var-Args(Variable Length Argument)

# positional parameter
# def posi(name,msg):
#     print(name,msg)
# print(posi('anuj' ,22))

# posi(name:"anuj")


# def squre_all(x):
#     sum=0,
#     for i in x:
#         sum=sum+i
#     return sum

# li =[1,2,3,4,5,6]
# print(squre_all(li))



'''print even number in continue method  '''
# 17/08/2026
# for i in range(20):
    # if i % 2 == 0:
    #     print(i)
    # else:
    #     continue

'''  Write a program to greet a specific user. '''
# while True :
#     n= input("enter name ")
#     if n == "anuj":
#         print("hello developer ")
#     else :
#         print("null")
#     break

        


''' Q .  Write a program (WAP) to create a menu-driven calculator using functions and a loop'''
# def addition(a, b):
#     return a + b 

# def subtraction(a, b):
#     return a - b

# def multiplication(a, b):
#     return a * b

# def division(a, b):
#     if b == 0:
#         return "Cannot divide by zero"
#     return a / b

# while True:
#     choice = int(input("Enter choice- 1 for addition, \n 2 for subtraction ,\n 3 for multiplication,\n 4 for division ,\n 5 for exit: "))

#     if choice == 5:
#         print("exit")
#         break
#     elif choice in (1, 2, 3, 4):
#         a = int(input("Enter Input: "))
#         b = int(input("Enter A Number: "))

#         match choice:
#             case 1:
#                 print("Addition Result:", addition(a, b))
#             case 2:
#                 print("Subtraction Result:", subtraction(a, b))
#             case 3:
#                 print("Multiplication Result:", multiplication(a, b))
#             case 4:
#                 print("Division Result:", division(a, b))
#     else:
#         print("Invalid choice, please select 1-5.")


'''Q... check the even or odd '''

# def isEven(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# li=[2,4,4,43,34,5,3]
# x = filter(isEven,li)
# for i in x :
#     print(i)

'''Q...FILTER IN FUNCTION'''
# def sequre(n):
#     if  ('a','e','i','o','u'):
#         return True
#     else:
#         return False
# li = ['a','s','f','h','e','i','o','u']

# print(sequre(li))

# '''Q...MAP() FUNCTION'''
# def sequre(n):
#     return n*n
# kk = [2,3,45,14,55,4,6,1]

# ak = map(sequre,kk)
# for i in ak:
#     print(i)


'''Q...'''