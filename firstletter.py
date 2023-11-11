import sys

# Check if a filename is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python capitalize_text.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        # Read the contents of the file and capitalize the first letter of each word
        file_contents = file.read()
        capitalized_contents = file_contents.title()
        print(capitalized_contents)
except FileNotFoundError:
    print(f"Error: The file '{input_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
