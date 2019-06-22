def fact(number):
    if number == 0:
        return 1
    else:
        product = number * fact(number-1)
        return product


# new pine for commenting
number2 = input("Enter number for factorial: ")

if number2.isnumeric():
    print(fact(int(number2)))
else:
    print("Enter a valid number")
