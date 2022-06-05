while True:
    print("______________________________")
    operator = input("Enter The Symbol +, -, *, /: ")

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    if operator == "+":
        print(num1, operator, num2, "=", num1 + num2)

    elif operator == "-":
        print(num1, operator, num2, "=", num1 - num2)

    elif operator == "*":
        print(num1, operator, num2, "=", num1 - num2)

    elif operator == "/":
        print(num1, operator, num2, "=", num1 - num2)

    else:
        print("COULD NOT REAL SYMBOL OR LETTER TRY AGAIN")
