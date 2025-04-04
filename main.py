import sys
from stats import get_num_words
from stats import get_dict
from stats import sort_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    dict_to_print = get_dict(text)
    sorted_dict = sort_count(dict_to_print)

    #print('============ BOOKBOT ============')
    #print('Analyzing book found at books/frankenstein.txt...')
    #print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    #print('--------- Character Count -------')    
    for i in sorted_dict.keys():
        if i.isalpha():
            print(f'{i}: {sorted_dict[i]}')
    #print('============= END ===============')

main()
