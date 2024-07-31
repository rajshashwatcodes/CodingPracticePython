import csv

def read_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def calculate_average_age(data):
    total_age = 0
    count = 0
    for row in data:
        total_age += int(row['Age'])
        count += 1
    return total_age / count if count != 0 else 0

def calculate_average_salary(data):
    total_salary = 0
    count = 0
    for row in data:
        total_salary += int(row['Salary'])
        count += 1
    return total_salary / count if count != 0 else 0

def main():
    file_path = 'data.csv'
    data = read_csv(file_path)
    
    avg_age = calculate_average_age(data)
    avg_salary = calculate_average_salary(data)
    
    print(f"Average Age: {avg_age:.2f}")
    print(f"Average Salary: {avg_salary:.2f}")

if __name__ == "__main__":
    main()
