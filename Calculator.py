print("Welcome to my primitive calculator!")
number1 = int(input("Please type in first number: "))
number2 = int(input("Please type in second number: "))
calculation = input("What kind of calculation would you like to perform?: ")
if calculation == "+":
    print(number1 + number2)
if calculation == "-":
    print(number1 - number2)
if calculation == "*":
    print(number1 * number2)
if calculation == "/":
    print(number1 // number2)