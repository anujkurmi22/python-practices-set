#8 aug 2026
"""
Q4. WAP to print  the two digit numbers
"""

# n= int(input("enter a number from 0 to 99:"))
# words =["zero", "one","two", "three", "four","five","six","seven"]
# tens =["","", "twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
# if n<20:
#     print(words[n])
# elif n<100:
#     tt = n//10
#     r = n % 10
#     print(tens[tt],words[r])
# else:
#     ("number must be 0 to 99")




"""
Q5. WAP to print the  0 to 999 in the user input
"""
n = int(input("enter a number from 0 to 999:"))
words =["zero", "one","two", "three", "four","five","six","seven","eight",
        "nine" ,"ten","eleven","twelve","thirteen","fourteen","fifteen",
        "sixteen","seventeen","eighteen","nineteen"]
tens =["","", "twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
if n == 0:
    print('ZERO')
if n<20:
    print(words[n])
elif n<100:
    a = n % 10
    b = n //10
    print(tens[a],words[b])
elif n<1000:
    t = n % 100
    r = n // 100 
    tt = t // 10
    x = t % 10
    if (t<20):
        print(words[r],"hundred",tens[tt],words[t])
    else:
        print(words[r],"hundred",tens[tt],words[x])
elif n < 10000:
    t = n % 1000
    r = n // 1000 
    tt = t // 100
    x = t % 100
    kk = x // 10
    ak = x % 10
    if(x<20):
        print(words[r],"thousand",words[tt],"hundred",tens[kk],words[x])
    else:
        print(words[r],"thousand",words[tt],"hundred",tens[kk],words[x])
        

else:
    print("number must be 0 to 999")