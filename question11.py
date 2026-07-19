#WAP to  accept the height of a person in cm  and categorize the person according their height .
height = int(input("enter height in cm : "))
if height<150:
    print("short")
elif height>=150 and height<=180:
    print("average height ")
else:
    print("tell")
