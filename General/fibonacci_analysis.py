import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = 10  # Change this to the desired number of Fibonacci numbers to generate and analyze

    print(f"Generating and analyzing the first {n} Fibonacci numbers:")
    
    start_time = time.time()
    for i in range(n):
        fibonacci_number = fibonacci(i)
        print(fibonacci_number, end=' ')
    end_time = time.time()
    
    elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"\nTime taken to generate {n} Fibonacci numbers: {elapsed_time:.2f} milliseconds")
    
    average_time = elapsed_time / n
    print(f"Average time to generate a Fibonacci number: {average_time:.2f} milliseconds")

if __name__ == "__main__":
    main()
