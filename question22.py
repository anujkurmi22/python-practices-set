'''    * 
      * * 
     * * * 
    * * * * 
   * * * * * 
 '''

# n=8
# for i in range(1,6):
#     for k in range (n, i ,-1):
#         print(" ", end="")
#     for j in range (1,i+1):
#         print("*", end=" ")

#     print()


# for i in range(1, 9):
#     for k in range (8 , i ,-1):
#         print(" * " , end="")
#         for j in range (1,i+2):
#             if i > 1 and j < 1:
#                 print(" " , end="")
#             else:
#                 print(" * " ,end="")
#         else:
#             print()

''''
      *      
     * *     
    *   *    
   *******   
  *       *  
 *         * 
*           *
'''
row = 7
for i in range(row):
    for j in range(2 * row - 1):
        
        if (j == row - 1 - i) or (j == row  - + i ):
            print("😍", end="")
       
        elif i == row // 2 and (row - 1 - i < j < row - 1 + i):
            print("😍", end="")
        else:
            print(" ", end="")
    print()

'''
* 
* * 
*   * 
*     * 
* * * * * 
'''

# for i in range (1,6):
#     for k in range (5,i-1):
#         print(" ",end=" ")
#     for j in range (1, i+1):
#         if i==5 or j==1 or j==i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()