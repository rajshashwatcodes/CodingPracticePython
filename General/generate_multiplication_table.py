def generate_multiplication_table(start, end):
    for i in range(start, end + 1):
        print(f"Multiplication table for {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()

def main():
    print("Welcome to the Multiplication Table Generator!")
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    if start > end:
        print("Error: Starting number cannot be greater than ending number.")
        return

    generate_multiplication_table(start, end)

if __name__ == "__main__":
    main()
