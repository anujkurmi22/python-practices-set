# WAP to find the calculate the speed .
distance = float(input("Enter distance traveled (km): "))
time = float(input("Enter time taken (Hrs): "))
if time == 0:
    print("Time cannot be zero.")
else:
    speed = distance / time
    print(f"Speed = {speed} km/h")

