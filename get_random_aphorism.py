import os
import sys
import random


def text_file_to_list():
    current_dir = os.getcwd()
    book_path = current_dir + str(r'/aphorisms.txt')
    print(book_path)
    with open(book_path, 'r', encoding='latin1') as book:
        aphorisms_list = [line.strip('-\n') for line in book if len(line) > 5]
    # print(aphorisms_list)
    return aphorisms_list


def print_random_quote(aphorisms_list):
    quote = 'a'
    while quote.encode("ascii", "ignore").decode("ascii") == quote:
        quote = aphorisms_list[random.randint(0, len(aphorisms_list))]
        if quote.encode("ascii", "ignore").decode("ascii") == quote:
            print(quote)
            break


def main():
    aphorisms_list = text_file_to_list()
    print_random_quote(aphorisms_list)

if __name__ == "__main__":
    main()
