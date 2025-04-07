def modify_content(line):
    # Converts text to uppercase
    return line.upper()

def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                modified_line = modify_content(line)
                outfile.write(modified_line)
        print(f"✅ Modified content has been written to '{output_filename}'")
    except FileNotFoundError:
        print(f"❌ File '{input_filename}' not found.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

def read_user_file():
    filename = input("📂 Enter the filename you want to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("📄 File Content:\n")
            print(content)
    except FileNotFoundError:
        print("❌ Error: File not found.")
    except PermissionError:
        print("🚫 Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("🔧 File Handling and Error Handling Assignment")
    print("1. Read and Modify a File")
    print("2. Read a User-Specified File with Error Handling")

    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        input_file = "input.txt"
        output_file = "output.txt"
        read_and_modify_file(input_file, output_file)
    elif choice == '2':
        read_user_file()
    else:
        print("❌ Invalid option. Please choose 1 or 2.")
2