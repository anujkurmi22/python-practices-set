# k = lambda x: x*x
# print(k(6))
# print("--*15")

# x = lambda k ,l : k if k>l else l
# print ("largest :" , x(20,30))
# print("---"*20)




# li =[1,23,34,54,65]
# q = map(lambda x : x*x ,li)
# for i in q:
#     print(i)



 '''recursion  function --> it is call it self again & again '''
 '''1 . factorial'''
# def factorial(n):
#     if n == 1: 
#         return 1
#     else:
#         return factorial(n-1)*n
# print(factorial(7))

# '''2 odd & even'''

def odd_even()(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


number = int(input("Enter a number: "))
odd_even()(number)