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

