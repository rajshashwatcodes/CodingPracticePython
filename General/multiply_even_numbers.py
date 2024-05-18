def multiply_even_numbers(start, end):
    result = 1
    for num in range(start, end + 1):
        if num % 2 == 0:
            result *= num
    return result

def main():
    print("Welcome to the Even Number Multiplication Program!")
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    if start > end:
        print("Error: Starting number cannot be greater than ending number.")
        return

    result = multiply_even_numbers(start, end)
    print(f"The product of all even numbers from {start} to {end} is: {result}")

if __name__ == "__main__":
    main()
