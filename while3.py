# Program to calculate discount based on sales amount

sales_amount = float(input("Enter sales amount "))

if sales_amount <3000:
   discount = 0
elif sales_amount <5000:
   discount = 5
elif sales_amount <10000:
   discount = 15
elif sales_amount <20000:
   discount = 18
else:
   discount = 22

discount_amount = sales_amount *(discount / 100)
final_amount = sales_amount - discount_amount

print(f"sales amount: RS. { sales_amount } ")
print(f"discount: { discount } % ")
print(f" discount amount: RS. { discount_amount } ")
print(f"final amount: RS. { final_amount } ")
