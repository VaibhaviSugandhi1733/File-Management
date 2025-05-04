import os
import shutil

def list_files(directory):
    try:
        files = os.listdir(directory)
        if not files:
            print("No files found in the directory")
        else:
            for file in files:
                print(file)
    except FileNotFoundError:
        print("Directory not found.")

def rename_file(directory, old_name, new_name):
    old_path = os.path.join(directory, old_name)
    new_path = os.path.join(directory, new_name)
    try:
        os.rename(old_path, new_path)
        print("File renamed successfully!")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)

def delete_path(directory, name):
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

def create_directory(directory, folder_name):
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
            directory = input("Enter directory path: ")
            list_files(directory)
        elif choice == "2":
            directory = input("Enter directory path: ")
            old_name = input("Enter old file name: ")
            new_name = input("Enter new file name: ")
            rename_file(directory, old_name, new_name)
        elif choice == "3":
            directory = input("Enter directory path: ")
            name = input("Enter file or directory name to delete: ")
            delete_path(directory, name)
        elif choice == "4":
            directory = input("Enter directory path: ")
            folder_name = input("Enter new folder name: ")
            create_directory(directory, folder_name)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

main()
