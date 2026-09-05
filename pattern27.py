num=int(input("Enter number : "))
for i in range(1,num+1):
    print(""*(2*num-i+1),end="")
    for j in range (1,i+1):
        print("A ",end=" ")
    print()
for i in range(1,num+3):
    print(""*(2*num-i+1),end="")
    for j in range(-1,i+1):
        print("A ",end=" ")
    print()