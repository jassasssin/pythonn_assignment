import json

# Read and modify a JSON file
def read_and_modify_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Modify a value (example: change the value of a specific key)
    data['key'] = 'new_value'  # Modify as needed

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
read_and_modify_json('data.json')  # Replace with your JSON file path
