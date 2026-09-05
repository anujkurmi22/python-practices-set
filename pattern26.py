"""
D D D D D
 C C C C C
  B B B B B
   A A A A A
"""
# num=4
# for i in range(1,num+1):
#     print(" "*(i-1),end="")
#     for j in range(2,num+2):
#         print(chr(65+num-i),end=" ")
#     for k in range(5,num+2):
#         print(chr(65+num-i),end="")
#     print()
"""
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
"""
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if(i%2!=0 and j%2!=0)or(i%2==0 and j%2==0):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()