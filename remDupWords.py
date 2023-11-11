import sys

# Function to remove duplicates from a list
def remove_duplicates(input_list):
    return list(set(input_list))

# Function to process the text and remove duplicate words
def process_text(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            words = content.split()

        unique_words = remove_duplicates(words)

        with open(output_filename, 'w') as output_file:
            output_file.write(' '.join(unique_words))

        print(f'Duplicate words removed. Unique words saved in {output_filename}')
    except FileNotFoundError:
        print(f'Error: File "{input_filename}" not found.')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py input_file output_file")
    else:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        process_text(input_filename, output_filename)
