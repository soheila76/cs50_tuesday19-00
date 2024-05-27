price = 50
total_paid = 0
coin = [5, 10, 25]

while price > 0:
    print(f"amount Due: {price}")
    pay = int(input("Enter your coin: "))
    if pay in coin:
        price = price - pay
        total_paid = total_paid + pay
        
if total_paid >= price :
    print(f"change owed : {total_paid - 50}")

