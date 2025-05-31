num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case '+':
        print("The result is {num1 + num2}.")
    case '-':
        print("The result is {num1 - num2}.")
    case '*':
        print("The result is {num1 * num2}.")
    case '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        else:
            print("The result is {num1 / num2}.")
