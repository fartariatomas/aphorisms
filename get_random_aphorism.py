import os
import sys
import random

def book_to_aphorisms(book_path):
    with open(book_path, 'r', encoding='latin1') as book:
        aphorisms_list = [line.strip('-\n') for line in book if len(line)>5]
    #print(aphorisms_list)
    return aphorisms_list

def main():
    book_path = str(
        r'C:/Users/tomas/Documents/MEGA/Python_projects/aphorisms/aphorisms.txt')
    aphorisms_list = book_to_aphorisms(book_path)
    quote = 'a'
    while quote.encode("ascii", "ignore").decode("ascii") == quote:
        quote = aphorisms_list[random.randint(0,len(aphorisms_list))]
        if quote.encode("ascii", "ignore").decode("ascii") == quote:
            print(quote)
            break
        else:
            quote = 'a'
if __name__ == "__main__":
    main()
