*********MOVIE PROJECT********


MENU_PROMPT =("\nEnter 'a' to add a movie, \n'l' to see your movies, \n'f' to find a movie by title, or \n'q' to quit: ")
movies = []


def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"\nTitle: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}\n")
    


def find_movie():
    search_title = input("Enter movie title you're looking for: ")

    for movie in movies:
        if movie["title"].lower() == search_title.lower():
            print_movie(movie)


user_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movie
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()







***BOOK DATABASE PROJECT***  
    
THE MAIN APP   
    
    
from utils import database


USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """





def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    database.add_book(name, author)


def list_books():
    for book in database.get_all_books():
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']} — Read: {read}")


def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')

    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')

    database.delete_book(name)
    



USING AN IN-MEMORY LIST AS A DATABASE

books = []


def create_book_table():
    pass


def get_all_books():
    return books


def insert_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True


def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name]


# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book) 
        
    
    
USING A TEXT FILE AS A DATABASE
    
    
    
books_file = 'books.txt'


def create_book_table():
    with open(books_file, 'w') as file:
        pass  # just to make sure the file is there


def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]


def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},0\n')


def _save_all_books(books): # this syntax says this private function should be used only within this file is NOT meant to be called externally
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)


# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)
    
    
    
USING A JSON FILE AS A DATABASE

import json


books_file = 'books.json'


def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)  # initialize file as empty list


def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def insert_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)# this syntax says this private function should be used only within this file is NOT meant to be called externally


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
    
    
    
USING A SQL DATABASE 


class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host
    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


from typing import List, Tuple

from utils.database_connection import DatabaseConnection

Book = Tuple(int, str, str, int)


def create_book_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        # SQLite automatically makes `integer primary key` row auto-incrementing (see link in further reading)
        cursor.execute('CREATE TABLE books (id integer primary key, name text, author text, read integer default 0)')


def get_all_books() -> List[Book]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
        #books = cursor.fetchall() a more simplified return
    return books


def insert_book(name: str, author: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books (name, author) VALUES (?, ?, 0)', (name, author))


def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))


def delete_book(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?', (name,))






BOOK WEB SCRAPING PROJECT 



class AllBooksPageLocators:
    BOOKS = 'div.page_inner section li.col-xs-6.col-sm-4.col-md-3.col-lg-3'
    PAGER = 'div.page_inner section ul.pager li.current'




class BookLocators:
    """
    Locators for an item in the HTML page.
    This allows us to easily see what our code will be looking at
    as well as change it quickly if we notice it is now different.
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'




import re
import logging

from locators.all_books_page import AllBooksPageLocators
from parsers.book import BookParser
from bs4 import BeautifulSoup

logger = logging.getLogger('scraping.all_books_page')


class AllBooksPage:
    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{AllBooksPageLocators.BOOKS}`')
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pages available...')
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        logger.info(f'Found number of catalogue pages available: `{content}`')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.info(f'Extracted number of pages as integer: `{pages}`.')
        return pages





import re
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')



class BookParser:
    """
    A class to take in an HTML page or content, and find properties of an item
    in it.
    """

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`')
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name} {self.price}, {self.rating} stars>'

    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookLocators.NAME_LOCATOR
        item_name = self.parent.select_one(locator).attrs['title']
        logger.info(f'Found book name, `{item_name}`.')
        return item_name

    @property
    def link(self):
        logger.debug('Finding book page link...')
        locator = BookLocators.LINK_LOCATOR
        item_url = self.parent.select_one(locator).attrs['href']
        logger.info(f'Found book page link, `{item_url}`.')
        return item_url

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string
        logger.debug(f'Item price element found, `{item_price}`')

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        price = float(matcher.group(1))
        logger.info(f'Found book price, `{price}`.')
        return price

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING_LOCATOR
        star_rating_element = self.parent.select_one(locator)
        classes = star_rating_element.attrs['class']
        rating_classes = filter(lambda x: x != 'star-rating', classes)
        rating_class = next(rating_classes)

        logger.debug(f'Found rating class, `{rating_class}`.')
        logger.debug('Converting to integer for sorting.')
        rating = BookParser.RATINGS.get(rating_class)
        logger.info(f'Found book rating, `{rating}`.')
        return rating




USING THE ABOVE SCRAPER WITH THE REQUESTS LIBRARY AND LOGGING

import requests
import logging
import time

from pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')
logger = logging.getLogger('scraping')

print('Loading books list...')
logger.info('Loading books list.')

logger.info('Requesting http://books.toscrape.com')
page_content = requests.get('http://books.toscrape.com').content

logger.debug('Creating AllBooksPage from page content.')
page = AllBooksPage(page_content)

_books = []

start = time.time()
logger.info(f'Going through {page.page_count} pages of books...')
for page_num in range(page.page_count):
    page_start = time.time()
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    logger.info(f'Requesting {url}')
    page_content = requests.get(url).content
    logger.debug('Creating AllBooksPage from page content.')
    page = AllBooksPage(page_content)
    print(f'{url} took {time.time() - page_start}')
    _books.extend(page.books)
print(f'Total took {time.time() - start}')

books = _books



USING THE ABOVE SCRAPER WITH ASYNCHRONOUS DEVELOPMENT AND LOGGING

"""
The speed at which you can request pages is not only a product of the speed of your Python program, but
also the speed of the server giving us the responses back including any artificial limitations that
have been put in place to prevent you from making too many requests at once.

"""

import asyncio
import aiohttp
import async_timeout
import requests
import logging
import time

from pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')
logger = logging.getLogger('scraping')

loop = asyncio.get_event_loop()

print('Loading books list...')
logger.info('Loading books list.')

logger.info('Requesting http://books.toscrape.com')
page_content = requests.get('http://books.toscrape.com').content

logger.debug('Creating AllBooksPage from page content.')
page = AllBooksPage(page_content)

_books = []


async def fetch_page(session, url):
    page_start = time.time()
    logger.info(f'Requesting {url}')
    async with session.get(url) as response:
        print(f'{url} took {time.time() - page_start}')
        return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        return await asyncio.gather(*tasks)


logger.info(f'Going through {page.page_count} pages of books...')


urls = [f'http://books.toscrape.com/catalogue/page-{page_num+1}.html' for page_num in range(page.page_count)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'Total page requests took {time.time() - start}')
for page_content in pages:
    logger.debug('Creating AllBooksPage from page content.')
    page = AllBooksPage(page_content)
    _books.extend(page.books)

books = _books








