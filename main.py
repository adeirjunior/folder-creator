import os
import json
import os.path as path

def create_folders_from_json(json_data):
    try:
        data = json.loads(json_data)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return

    network_path = r'C:\your\folder\path'

    for item in data:
        if "name" in item:
            folder_name = item["name"]
            folder_path = path.join(network_path, folder_name)
            try:
                os.makedirs(folder_path, exist_ok=True)
                print(f"Folder '{folder_name}' created successfully.")
            except FileExistsError:
                print(f"Folder '{folder_name}' already exists.")
            except Exception as e:
                print(f"Error creating folder '{folder_name}': {e}")

if __name__ == "__main__":
    json_file = 'file_path.json'

    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            json_data = file.read()
            create_folders_from_json(json_data)
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
