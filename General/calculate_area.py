import math

def calculate_area(radius):
    return math.pi * radius**2

def main():
    print("Welcome to the Circle Area Calculator!")
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_area(radius)
    print("The area of the circle with radius", radius, "is:", area)

if __name__ == "__main__":
    main()
