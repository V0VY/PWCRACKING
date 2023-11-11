# import libraries
import argparse
import random

# define a function to add all combinations from 111-999 to words
def add_all_combinations(words):
    result = []
    for word in words:
        for num in range(0, 100):
            result.append(word + str(num))
    return result

# create and parse command-line arguments
parser = argparse.ArgumentParser(description="Add all combinations from 111 to 999 to a list of words from a text file")
parser.add_argument("word_file", type=str, help="Path to the text file containing a list of words")
args = parser.parse_args()

# Read the list of words from the provided text file
with open(args.word_file, 'r') as file:
    words = [line.strip() for line in file]

# Call the function to add all combinations from 111-999
resulting_words = add_all_combinations(words)

# Print the resulting words
for word in resulting_words:
    print(word)
