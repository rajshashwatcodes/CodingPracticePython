def find_largest_smallest(numbers):
    if not numbers:
        return None, None
    largest = smallest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    return largest, smallest

def main():
    print("Welcome to the Largest and Smallest Element Finder!")
    numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

    largest, smallest = find_largest_smallest(numbers)
    if largest is not None and smallest is not None:
        print(f"The largest number in the list is: {largest}")
        print(f"The smallest number in the list is: {smallest}")
    else:
        print("Error: Please enter a valid list of numbers.")

if __name__ == "__main__":
    main()
