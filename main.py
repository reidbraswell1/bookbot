import os
import sys
from pathlib import Path
from stats import get_num_words

DEBUG = False

def main():
    cmd_args: list[str] = sys.argv
    if len(cmd_args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = cmd_args[1]
    current_path = Path.cwd()
    with open(current_path/book) as f:
        file_contents = f.read()
        
        words = get_num_words(file_contents)
        #print("Words=",words)

        letters = count_all_letters(file_contents)
        #print(f"All letters={letters}")
        
        letters = count_alpha_letters(file_contents)
        print_report_by_number(letters, words, book)
        print_report_by_letter(letters,words, book)

        # Non Alpha Character Report
        #letters = count_non_alpha_letters(file_contents)
        #print_report_by_number(letters, words)
        #print_report_by_letter(letters, words)

# Count the number of letters in a string
def count_all_letters(string):
    
    dict = {}

    for letter in string.lower():
        if letter in dict:
            dict[letter] = dict[letter] + 1
        else:
            dict[letter] = 1
    return dict

# Count the number of alpha letters in a string
def count_alpha_letters(string):
    
    dict = {}

    for letter in string.lower():
        if letter.isalpha():
            if letter in dict:
                dict[letter] = dict[letter] + 1
            else:
                dict[letter] = 1
    return dict

# Count the number of non-alpha letters in a string
def count_non_alpha_letters(string):
    
    dict = {}

    for letter in string.lower():
        if not letter.isalpha():
            if letter in dict:
                dict[letter] = dict[letter] + 1
            else:
                dict[letter] = 1
    return dict

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on_num(dict):
    return dict["num"]

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on_ltr(dict):
    return dict["ltr"]



# Total report of the number of times a letter occurs 
# in the book sorted by number
def print_report_by_number(dict, words, book):

    report = []

    for (key, value) in dict.items():
        report.append({"ltr":key, "num":value})
        report.sort(reverse=True, key=sort_on_num)
    print(f"\n--- Begin report 'by count' of {book} ---")
    print(f"Found {words} total words found in the document")
    for dict in report:
        print(f"{dict['ltr']}: {dict['num']}")
    print("--- End report ---")

# Total report of the number of times a letter occurs 
# in the book sorted by letter
def print_report_by_letter(dict, words, book):

    report = []

    for (key, value) in dict.items():
        report.append({"ltr":key, "num":value})
        report.sort(reverse=False, key=sort_on_ltr)
    print(f"\n--- Begin report 'by letter' of {book} ---")
    print(f"{words} words found in the document")
    for dict in report:
        print(f"The '{dict['ltr']}' chacter was found {dict['num']} times")
    print("--- End report ---")



# Ensure main() runs only when the script is executed directly
if __name__ == "__main__":
    if DEBUG:
        print(f"__name__={__name__}")
        current_directory = os.getcwd() 
        print("Current Directory:",current_directory) 
        current_directory = Path.cwd()
        print("Current Directory:", current_directory)
    main()
