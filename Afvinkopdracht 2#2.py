# 2 sales prediction
sales = input(str("What is the projected amount of total sales?\n"))
if isinstance(sales, int, float) == False:
    print("Invalid input")
    exit()
profit = 0.23 * sales
print("expected profit = " profit)