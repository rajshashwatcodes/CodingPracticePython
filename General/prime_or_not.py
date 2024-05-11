def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    num = int(input("Enter a number to check if it's prime: "))
    if is_prime(num):
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")

if __name__ == "__main__":
    main()
