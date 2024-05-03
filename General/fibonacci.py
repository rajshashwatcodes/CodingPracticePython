def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]  # Initialize Fibonacci sequence with first two numbers

    while True:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # Calculate next Fibonacci number
        if next_number > limit:  # Check if the next number exceeds the limit
            break
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

def main():
    limit = int(input("Enter the limit for Fibonacci numbers: "))
    fibonacci_sequence = generate_fibonacci(limit)
    print("Fibonacci numbers up to", limit, "are:", fibonacci_sequence)

if __name__ == "__main__":
    main()
