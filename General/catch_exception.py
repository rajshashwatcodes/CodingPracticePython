def divide_numbers(dividend, divisor):
    try:
        result = dividend / divisor
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Finally block executed.")

# Test the divide_numbers function
dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))
divide_numbers(dividend, divisor)
