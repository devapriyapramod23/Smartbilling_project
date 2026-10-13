#CUSTOMER A : ANIL

print("="*50)
print("KERALA FRESH MART".center(50))
print("SMART BILLING".center(50))
print("="*50)
name=input("Customer name:")
item=input("Item name:")
Qty=int(input("Quantity:"))
Price=int(input("Price per unit (Rs):"))
LM=input("Loyalty member?[y/n]:")
pm=input("Payment mode (cash/upi/card):")
print()

print(f"{"Customer:":<9}{name}")
print("-"*50)
Amount=Qty*Price
print(f"{"Item":<19}{"Qty":^7}{"Price":^7}{"Amount":>17}")
print(f"{item:<19}{Qty:^7}{Price:^7}{Amount:>17,.2f}")
print("-"*50)
print(f"{"Amount":<40}{Amount:>10,.2f}")
if Amount>=2000:
  rate=10
elif Amount>=1000:
  rate=5
elif Amount>=500:
  rate=2
else:
  rate=0
Discount=Amount*rate/100
print(f"{"Discount rate:":<46}{rate:>3}%")
print(f"{"Discount:":<40}{Discount:>10}")
if LM.lower()=="y" and Amount>=500:
  bonus=25
else:
  bonus=0
  print(f"{"Loyalty bonus":46}{bonus:>3.2f}")
Tax=Amount-Discount-bonus
print(f"{"Taxable Amount":<40}{Tax:>10,.2f}")
gst=Tax*5/100
print(f"{"GST(5%)":<40}{gst:>10.2f}")
Total=Tax+gst
print(f"{'Grand Total:':<40}{Total:>10,.2f}")
print("="*50)
if Qty%12==0:
  print("Bonus:free cloth bag with this order")
else:
  pass
if pm=="cash" and Total>=10000:
  print("Cash limit of Rs 10,000 exceeded:Please pay by UPI or card")
elif  pm in ("cash","upi","card"):
  print(f"Payment accepted via {pm.upper()}")
else:
  print("Invalid payment mode.Bill not settled")

