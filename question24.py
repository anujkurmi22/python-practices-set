''''
27 july 2026 infoviaan 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()



'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15

'''
# c=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(c,end=" ")
#         c=c+1
#     print()


'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 
1 2 3 4 5 6 7 8 9 
'''
# for i in range (1,10):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

i = 1
c = 1
while i < 10:
    j = 1
    while j<=i:
        print(c,end=" ")
        c=c+1
        j=j+1
    print()
    i= i+1

"""
*  *  *  
*  *  *  
*  *  *  
"""

# for i in range (1,4):
#     for j in range(1,4):
#         print("* ",end=" ")
#     print()