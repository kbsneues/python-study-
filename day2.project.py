print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

contain_tip_bill = bill * (tip / 100 + 1)

each_total_pay = contain_tip_bill / people 

result = round(each_total_pay,2)
result = "{:.2f}".format(each_total_pay)

print(f"Each person should pay: ${result}")

