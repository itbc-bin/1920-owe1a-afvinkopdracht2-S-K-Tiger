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