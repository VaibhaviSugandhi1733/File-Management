import os
import shutil

def list_files():
    directory = input("Enter directory path: ")
    try:
        files = os.listdir(directory)
        if not files:
            print("No files found in the directory")
        else:
            for file in files:
                print(file)
    except FileNotFoundError:
        print("Directory not found.")
    except Exception as e:
        print("Error:", e)

def rename_file():
    directory = input("Enter directory path: ")
    old_name = input("Enter the current filename: ")
    new_name = input("Enter the new filename: ")
    old_path = os.path.join(directory, old_name)
    new_path = os.path.join(directory, new_name)
    try:
        os.rename(old_path, new_path)
        print("File renamed successfully!")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)

def delete_path():
    directory = input("Enter directory path: ")
    name = input("Enter the file or folder name to delete: ")
    path = os.path.join(directory, name)
    try:
        if os.path.isfile(path):
            os.remove(path)
            print("File deleted successfully!")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print("Directory deleted successfully!")
        else:
            print("The specified path does not exist.")
    except Exception as e:
        print("Error:", e)

def create_directory():
    directory = input("Enter parent directory path: ")
    folder_name = input("Enter new folder name: ")
    path = os.path.join(directory, folder_name)
    try:
        os.makedirs(path, exist_ok=True)
        print("Directory created successfully!")
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        print("\nFile Management System")
        print("1. List Files")
        print("2. Rename File")
        print("3. Delete File/Directory")
        print("4. Create Directory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_files()
        elif choice == "2":
            rename_file()
        elif choice == "3":
            delete_path()
        elif choice == "4":
            create_directory()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()
