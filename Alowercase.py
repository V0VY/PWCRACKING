import sys

# Check if a filename is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python lowercase_text.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        # Read the contents of the file and convert to lowercase
        file_contents = file.read()
        lowercase_contents = file_contents.lower()
        print(lowercase_contents)
except FileNotFoundError:
    print(f"Error: The file '{input_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
