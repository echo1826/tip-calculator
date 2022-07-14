from posixpath import split


print("welcome to the tip calculator")

bill = float(input("What was the total bill? "))

tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

people_split = int(input("How many people to split the bill? "))

tip_decimal = tip_percentage/100

if people_split != 0:
    split_bill = (bill/people_split) * (1+tip_decimal)
else:
    split_bill = bill * (1 + tip_decimal)

print(round(split_bill, 2))