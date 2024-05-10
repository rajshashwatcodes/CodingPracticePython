def square_sequence(n):
    return [i**2 for i in range(1, n+1)]

def main():
    n = int(input("Enter the number of terms in the square sequence: "))
    if n <= 0:
        print("Number of terms must be a positive integer.")
    else:
        sequence = square_sequence(n)
        print("Square sequence with", n, "terms:", sequence)

if __name__ == "__main__":
    main()
