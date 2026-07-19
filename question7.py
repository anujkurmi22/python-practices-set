# Q1 WAP to print the employee detail in the all.

principle_amount = float(input("Enter principal amount: "))
interest_rate = float(input("Enter interest rate: "))
time_duration = float(input("Enter time duration in years: "))
                      
simple_interest = (principle_amount * interest_rate * time_duration) / 100

final_amount = principle_amount + simple_interest

print("Principal Amount:", principle_amount)
print("Interest Rate:", interest_rate, "%")
print("Time Duration:", time_duration, "years")
print("Simple Interest:", simple_interest)
print("Final Amount:", final_amount)