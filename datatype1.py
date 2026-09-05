'''numeric data type --> 
1.integers(1,2,34,5,70,9,35)
2.float (34.43,4,754.323538)
3 .complex (i+5j)
4.boolen(true or false)'''

"""
1. set is collection of unique elements
2.set is mutable
3.set is unordered collection of elements
4.set is iterable   
5.set is not subscriptable,
6. set is not indexable, 
"""
'''if you want to create empty set then you have to use set()
function, if you use {} then it will create empty dictionary  '''
# s = set()
# ss = {1,2,3,4,5,65,6,7,8,9} #set with elements
# print(type(ss))
# print(ss)
# for value in ss:
#     print(value)
# ss.add(1300)
# ss.add(14)
# ss.add(105)
# print(ss)
# ss.remove(105)
# print(ss)
# print(ss.pop())
# print(ss)
# ss.clear()
# print(ss)

# x = {1,2,3,4,5,6,7,8,9}
# y = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
# print(x.union(y))
# print(x.union(x))
# print(x.intersection(x))
# print(x.intersection(y))
# print(x.difference(y))
# print(y.difference(x))
# x.update(y)
# print(x,y)


# cities ={"sagar","bhopal","indore","delhi","mumbai"}
# cities2={"sagar","madras","london"}
# cities3 = cities.difference(cities2)
# print(cities3)

# cities ={"sagar","bhopal","indore","delhi","mumbai"}
# cities2={"shgs","madras","london"}
# print(cities.isdisjoint(cities2))

'''
Frozenset is immutable set, it means we cannot add or remove elements from the set.

'''
# fs = frozenset([1,2,3,4,5,6,7,8,9,"anuj","cat","gullu"])
# print(type(fs))
# print(fs)
# fs.add(4,443,54)                    #AttributeError: 'frozenset' object has no attribute 'add'
# print(fs)

'''Dictionary is mutable, it means we can add or remove elements from the dictionary.  '''
# d = {'name': 'anuj', 'age': 22, 'address': 'indore', 'roll': 2253}
# print(type(d))
# d['friend']= 'sagar'
# d.update({'friend':'kk bhai', 'course': 'python'})

# print(d)



'''
Function is a block of code
1. No return value and no argument
2. no return value but with argument
3. return value but  no argument 
4. return value but with argument
'''
# 1. No return value and no argument
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

def anuj():
   print("i am anuj kurmi")
   print('i am from sagar')
   print()
anuj()

print('__'* 20)

# a,b = 100,50
a = int(input("enter two value"))
b = int(input("enter number"))
print('additon:', a+b),
print('subtraction:',a-b),
print("multiplication :" ,a*b),
print("division:",a//b)
print("__"*20)

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
#     print('Hello MR.',name,'!',msg)
# wish('Anuj','you are  Software Developer.....')
# # print("_*_")

""" 3 Return value but no argument"""

# def count():
#     age 18 
# print(count())



# c= count()
# print("total count" :c)


# def fact(n):
#     fa=1
#     for i in range (1,n+1):
#         fa*1
#     return fact
# print(factorial(5))


# def getAge(birthAge):
#     return 2026-birthAge
# print("your age is :" , getAge(2004))

# def info (name,age,address):
#     return name is "Anuj Kurmi ",age is" 22" ,address is "vijay nagar indore "
# print()


# def getAge(birthAge):
#     return 2026-birthAge
# print("you Age is :", getAge(2004))


# def number(a,b):
#     sum_result= a+b
#     return sum_result
# total= number(10,29)
# print("The total is " ,total)