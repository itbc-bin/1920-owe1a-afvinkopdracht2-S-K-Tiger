# 2 sales prediction
sales = float(input(str("What is the projected amount of total sales?\n")))
if isinstance(sales, (int, float)) != True:
    print("Invalid input")
    exit()
profit = 0.23 * sales
print("expected profit = " + str(profit))