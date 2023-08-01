# Defining a function to find the factorial of a number using recursion.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Taking input from the user:
num = int(input("Enter a number: "))

# Checking if the number is negative or not:
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print("Factorial of", num, "is", result)
