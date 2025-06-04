def perform_operation(num1, num2, operation):
    """Perform basic arithmetic operations."""
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            try:
                result = num1 / num2
            except ZeroDivisionError:
                return "Cannot divide by zero."
            else:
                return result


if __name__ == "__main__":
    perform_operation()
