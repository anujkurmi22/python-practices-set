
# WAP a program to find and print the sum of all even number and the sum of all odd number from  1 to 100 .
evensum=0 
oddsum=0 
i = 1
while i<= 100:
    if 1 % 2 == 0:
        evensum += i
    else :
        oddsum += i 
    i = i + 1

    print(" total sum of all even  no. from 1 to 100: " , evensum)
    print("total sum of all even no. from 1 to 100: " , oddsum) 