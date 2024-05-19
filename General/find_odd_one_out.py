def find_odd_one_out(numbers):
    # Initialize dictionaries to count the occurrences of each number
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Find the number with odd occurrences
    odd_one_out = None
    for num, count in count_dict.items():
        if count % 2 != 0:
            odd_one_out = num
            break

    return odd_one_out

def main():
    print("Welcome to the Odd One Out Finder!")
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]

    odd_one_out = find_odd_one_out(numbers)
    if odd_one_out is not None:
        print(f"The odd one out in the list is: {odd_one_out}")
    else:
        print("There is no odd one out in the list.")

if __name__ == "__main__":
    main()
