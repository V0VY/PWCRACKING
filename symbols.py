# import libraries
import argparse

# define a function to add special characters after the second letter in words
def add_special_chars_after_second_letter(words, special_chars):
    result = []
    for word in words:
        for special_char in special_chars:
            for i in range(len(word)):
                result_word = word[:i+2] + special_char + word[i+2:]
                result.append(result_word)
    return result

# create and parse command-line arguments
parser = argparse.ArgumentParser(description="Add special characters after the second letter in a list of words from a text file")
parser.add_argument("word_file", type=str, help="Path to the text file containing a list of words")
args = parser.parse_args()

# Read the list of words from the provided text file
with open(args.word_file, 'r') as file:
    words = [line.strip() for line in file]

# Define a list of special characters
special_chars = ["@", "#", "!", "$", "%", "&", "*", "(", ")", "_", "-", "+", "=", "[", "]", "{", "}", "<", ">", "/", "?", ":", ";", ".", ",", "|", "\\"]

# Call the function to add special characters after the second letter
resulting_words = add_special_chars_after_second_letter(words, special_chars)

# Print the resulting words
for word in resulting_words:
    print(word)
for word in resulting_words:
    print(word)
