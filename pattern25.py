"""
   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   * 
"""
# n = int(input("enter input rows: "))
# for i in range(n):
#     print(" "*(n-i-1)+"* "*(i+1))
# for i  in range(n-1):
#      print(" "*(i+1) +"* "*(n-i-1))

# n = int(input("enter input rows: "))
# for i in range(n):

#     print(" "*(i)+"v "*(n-i-1))
# for j in range (n):
#     print(" "*(j)+" "*(n-i-1))

"""
A
BB
CCC
DDDD
EEEEE
FFFFFF
"""
# n = 6
# for i in range(1,n + 1):
#     print(chr(64+i )*i)
# for j in range (1,n -1):
#         print(chr(64+i )*i , end=" ")
    

n=5
for i in range(1,n+1):
    for j in range(i):

      print(chr(65+j),end="")
      print()