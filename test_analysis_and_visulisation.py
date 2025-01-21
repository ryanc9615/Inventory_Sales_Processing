import string

def get_file_path():
    while True:
        file_path = input("Please enter the file path: ")
        try:
            with open(file_path, 'r') as file: 
                return file_path
        except FileNotFoundError: 
            print("Error: File not found. Please try again.")
        except PermissionError:
            print("Error: Permission denied. Please try again.")
        except Exception as e:
            print(f"Error: {str(e)}. Please try again.")

file_path = get_file_path()

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content
