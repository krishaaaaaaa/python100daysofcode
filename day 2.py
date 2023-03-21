
print("Welcome to Tip Calculator.")
a = float(input("What was the Total Bill? "))
b = float(input("What percentage would you like to give? 10, 12 or 15? "))
c = float(input("How many people to split the bill? "))
d =(a*(b/100)) +a
e = d/c
print(f"Each person should pay: ${round(e,2)}")
