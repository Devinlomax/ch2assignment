salesTax = 0.095
item1 = float(input("What is the price of item1?"))
item2 = float(input("What is the price of item2?"))
item3 = float(input("What is the price of item3?"))
item4 = float(input("What is the price of item4?"))
item5 = float(input("What is the price of item5?"))
var = item1+item2+item3+item4+item5 *salesTax
print("your total is",round( var, 2))