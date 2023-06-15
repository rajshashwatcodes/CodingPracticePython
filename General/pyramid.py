# a program to print the following pattern
# 1
# 12
# 123
# 1234
# 12345
# 1234
# 123
# 12
# 1

# Get height from user
height = int(input("Height: "))
# Set counter
counter = 1
# Set while loop
while counter <= height:
    # Set inner counter
    inner_counter = 1
    # Set while loop
    while inner_counter <= counter:
        # Print inner counter
        print(inner_counter, end="")
        # Increment inner counter
        inner_counter += 1
    # Print new line
    print()
    # Increment counter
    counter += 1
# Set counter
counter = height - 1
# Set while loop
while counter >= 1:
    # Set inner counter
    inner_counter = 1
    # Set while loop
    while inner_counter <= counter:
        # Print inner counter
        print(inner_counter, end="")
        # Increment inner counter
        inner_counter += 1
    # Print new line
    print()
    # Decrement counter
    counter -= 1
