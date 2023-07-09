def calculate_mean(numbers):
    if len(numbers) == 0:
        return 0  # Return 0 if the list is empty
    
    total = sum(numbers)
    mean = total / len(numbers)
    return mean

# Example usage
number_list = [1, 2, 3, 4, 5]
mean_value = calculate_mean(number_list)
print("Mean:", mean_value)
