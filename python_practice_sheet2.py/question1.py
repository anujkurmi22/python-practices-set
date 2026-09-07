"""
write a program to print day of a week name .
"""
day = int(input("enter day"))
match day:
    case 1:
        print("monday")
    case 2:
        print("tues")
    case 3:
        print("wed")
    case 4:
        print("ther")
    case 5 :
        print("frid")
    case 6:
        print("sater")
    case 7:
        print("sunday")
    case _ :
        print("add a valid numbe of day")

