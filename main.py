print("\n====== SHOPPING BILL CALCULATOR=====")
name=input("Enter product name:")
price=float(input("Enter price:"))
quantity=int(input("Enter quantity:"))
subtotal=price * quantity
discount=subtotal * 0.1
finalamount=subtotal-discount

print("\n=====YOUR BILL=====")

print(f"Product:{name}")
print(f"Price:{price}")
print(f"Quantity:{quantity}")
print(f"Subtotal:{subtotal}")
print(f"Discount:{discount}")
print(f"Final Amount:{finalamount}")

