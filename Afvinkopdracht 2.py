# 1 personal information
name = "Lars [REDACTED]"
adress = {"city": "[REDACTED]", "state": "Noord-Brabant", "ZIP": "[REDACTED]"}
phoneNR = "+31 6 [REDACTED]"
CollageMajor = "HAVO"
print("name = " + name + "\nstate = " + adress["state"] + "\nadress = " + adress["city"] + "\nZIP = " + adress["ZIP"] + "\nphone number = " + phoneNR + "\nCollage major = " + CollageMajor)

# 2 sales prediction
sales = float(input(str("What is the projected amount of total sales?\n")))
if isinstance(sales, (int, float)) != True:
    print("Invalid input")
    exit()
profit = 0.23 * sales
print("expected profit = " + str(profit))

# 3 Pounds to kilograms
retartUnit = float(input(str("Enter pounds for conversion: ")))
nonRetart = 0.454 * retartUnit
print(str(retartUnit) + " = ~" + str(nonRetart) + " kg")

# 4 Total
I1 = float(input(str("Prize of item 1/5 = ")))
I2 = float(input(str("Prize of item 2/5 = ")))
I3 = float(input(str("Prize of item 3/5 = ")))
I4 = float(input(str("Prize of item 4/5 = ")))
I5 = float(input(str("Prize of item 5/5 = ")))
subTot = I1 + I2 + I3 + I4 + I5
print("The subtotal is " + str(subTot))
saletax = 0.07
print("The saletax is " + str(saletax * 100) + "%")
tot = subTot * saletax
print("Your total is " + str(tot))

# 5 Distance Traveled
print("When going 70 miles/hour you wil have traveled:")
print(str(6 * 70) + " miles in 6 hours")
print(str(10 * 70) + " miles in 10 hours")
print(str(15 * 70) + " miles in 15 hours")

# 7 Miles-per-Gallon
retartDis = float(input(str("How many miles have you driven? ")))
retartVol = float(input(str("How many gallons of gas did your car consume during that time? ")))
MPG = retartDis / retartVol
print("Your MPG is " + str(MPG))

# 10 Ingredient Adjuster
sugarCupsPerCookie = 1.5 / 48
buttercupsPerCookie = 1 / 48
flourCupsPerCookie = 2.75 / 48
cookies = int(input(str("How many cookies doe you want to make? ")))
if cookies < 0:
    print("invalid amount")
else:
    print("You wil need:\n" + str(sugarCupsPerCookie * cookies) + " cups of sugar\n" + str(buttercupsPerCookie * cookies) + " cups of butter\n" + str(flourCupsPerCookie * cookies) + " cups of flour")
#By Lars Weijenborg
