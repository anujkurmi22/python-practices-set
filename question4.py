 #  question 4 WAP to find the leap year or not .

year = int(input("Enter year : "))
if (year % 400== 0 ) and (year % 4 == 0 or year % 100 != 0):
    print("this is leap  year")
else:
   print("this is not leap year")