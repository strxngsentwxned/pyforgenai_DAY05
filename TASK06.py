import os

while True:
    menu()

def menu():
    print("Menu:")
    print("1. Create new text file")
    print("2. Read existing file")
    print("3. Append to file")
    print("4. Delete file")
    print("5. List all .txt files in directory")
    print("6. Exit")
    choice = int(input("Please select an option: "))
    if choice == 1:
        create_file()
    elif choice == 2:
        read_file()
    elif choice == 3:
        append_to_file()
    elif choice == 4:
        delete_file()
    elif choice == 5:
        list_txt_files()
    elif choice == 6:
        print("Exiting...")
        exit()
    else:
        print("Invalid option. Please try again.")

def create_file():
    filename = input("Enter the name of the file to create (with .txt extension): ")
    with open(filename, 'w') as file:
        content = input("Enter the content to write to the file: ")
        file.write(content)
    print(f"File '{filename}' created successfully.")

def read_file():
    filename = input("Enter the name of the file to read (with .txt extension): ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def append_to_file():
    filename = input("Enter the name of the file to append to (with .txt extension): ")
    try:
        with open(filename, 'a') as file:
            content = input("Enter the content to append to the file: ")
            file.write(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def delete_file():
    filename = input("Enter the name of the file to delete (with .txt extension): ")
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def list_txt_files():
    txt_files = [f for f in os.listdir() if f.endswith('.txt')]
    if txt_files:
        print("Text files in the current directory:")
        for file in txt_files:
            print(file)
    else:
        print("No .txt files found in the current directory.")
