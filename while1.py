#WAP to calculate the area of circle , rectangle & trangle
print("Enter 1 to calculate area of circle:")
print("Enter 2 to calculate area of tringle:")
print("Enter 3 to calculate area of rectangle:")
print("Enter 4 to calculate area of squeree:")

count = input("Enter value:")
if count == '1':
    r = float(input("enter radious: "))
    area = 3.14 * r * r
    print("Area  of circle is ", area)
elif count == '2':
    hight = float(input("enter hight: "))
    base = float(input("enter base :"))
    area = base * hight    
    print("Area of  tringle is ", area)
elif count == '3':
    len = float(input("Enter lenth of the rectangle: "))
    hight = float(input("Enter area of rectangle:"))
    area = len * hight
    print("Area of rectangle:", area)
elif count == '4':
    arm = float(input("Enter of squre :"))
    area = arm * arm 
    print("Area of squre is ", area)
else:
    print("You enter wrong input",count)
