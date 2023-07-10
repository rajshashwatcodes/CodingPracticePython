def divide_numbers(a, b):
    try:
        result = a / b
        print("The result of the division is:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except TypeError:
        print("Error: Invalid operand type!")
    except Exception as e:
        print("An error occurred:", str(e))

# Example usages
divide_numbers(10, 2)  # Valid division
divide_numbers(10, 0)  # Division by zero
divide_numbers(10, '2')  # Invalid operand type
