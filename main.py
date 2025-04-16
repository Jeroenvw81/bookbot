import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import (
    get_word_count,
    get_character_count,
    get_sorted_character_list,
)

def main():
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    word_count = get_word_count(text)
    character_dict = get_character_count(text)
    char_sorted_list = get_sorted_character_list(character_dict)
    print_report(path_to_file, word_count, char_sorted_list)

def print_report(path_to_file, word_count, char_sorted_list): 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in char_sorted_list:
        print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()



main()
