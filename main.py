import sys
from stats import get_num_words, count_characters, sort_letters

def get_book_text(path):
    with open(path) as f:
        return(f.read())

def print_result(count_string, list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at ...")
    print("----------- Word Count ----------")
    print(count_string)
    print("--------- Character Count -------")
    for letter in list:
        print(f"{letter['char']}: {letter['num']}")       
    print("============= END ===============")

    

def main():
    list_of_arguments = sys.argv
    if len(list_of_arguments) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    amount_of_text = get_num_words(get_book_text(list_of_arguments[1]))
    character_count = count_characters(get_book_text(list_of_arguments[1]))
    sorted_list = sort_letters(character_count)
    print_result(amount_of_text, sorted_list)



main()