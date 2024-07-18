# Creating an awesome Python list with various data types
awesome_list = [
    42,                            # Integer
    3.14,                          # Float
    "Hello, World!",               # String
    True,                          # Boolean
    [1, 2, 3],                     # List within a list
    {"key": "value"},              # Dictionary
    (4, 5, 6),                     # Tuple
    {7, 8, 9},                     # Set
    lambda x: x * 2,               # Lambda function
    None                           # NoneType
]

# Accessing elements
print("First element:", awesome_list[0])
print("Fourth element:", awesome_list[3])
print("Nested list:", awesome_list[4])

# Modifying elements
awesome_list[0] = 99
print("Modified list:", awesome_list)

# Adding elements
awesome_list.append("New Element")
print("After appending:", awesome_list)

# Removing elements
awesome_list.remove(3.14)
print("After removing an element:", awesome_list)

# List comprehension
squares = [x**2 for x in range(10)]
print("List of squares:", squares)

# Using a lambda function from the list
result = awesome_list 
print("Result of lambda function:", result)

# Iterating through the list
for item in awesome_list:
    print("Item:", item)
