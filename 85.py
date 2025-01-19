import csv

def read_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

# Example usage
read_csv('example.csv')  # Replace with your CSV file path
