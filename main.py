from stats import word_count
from stats import character_count
from stats import sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_count(text)
    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    Found {num_words} total words""")
    character_list = character_count(text)
    sorted_characters = sorted_list(character_list)
    print("--------- Character Count -------")
    for char, count in sorted_characters:
        if char.isalpha():
            print(f"{char}: {count}")

main()
