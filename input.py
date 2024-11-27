def modify_file_content(input_file, output_file):
   
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as infile:
            content = infile.readlines()  # Read all lines into a list

        modified_content = [line.strip() + " - Modified\n" for line in content]

        with open(output_file, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Content has been successfully modified and written to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# File paths (can be updated to user input or fixed file paths)
input_file = input("Enter the name of the file to read from: ")
output_file = input("Enter the name of the new file to write to: ")

modify_file_content(input_file, output_file)


def read_file_with_error_handling():
   
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Call the function
read_file_with_error_handling()
