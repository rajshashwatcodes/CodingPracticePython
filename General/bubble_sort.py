# Given list of numbers:
input_list = [64, 34, 25, 12, 22, 11, 90]
print("Original List:", input_list)

n = len(input_list) # Sort the list in ascending order using bubble sort

for i in range(n):
    # Flag to check if any swap is performed in the current pass
    swapped = False
    
    # Last i elements are already in place after i-th pass
    for j in range(0, n-i-1):
        # Swap if the element found is greater than the next element
        if input_list[j] > input_list[j+1]:
            input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
            swapped = True

    # If no two elements were swapped in the inner loop, the list is already sorted
    if not swapped:
        break

print("Sorted List:", input_list)
