# 10 Ingredient Adjuster
sugarCupsPerCookie = 1.5 / 48
buttercupsPerCookie = 1 / 48
flourCupsPerCookie = 2.75 / 48
cookies = int(input(str("How many cookies doe you want to make? ")))
if cookies < 0:
    print("invalid amount")
else:
    print("You wil need:\n" + str(sugarCupsPerCookie * cookies) + " cups of sugar\n" + str(buttercupsPerCookie * cookies) + " cups of butter\n" + str(flourCupsPerCookie * cookies) + " cups of flour")