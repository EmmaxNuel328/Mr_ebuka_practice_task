import random
def suggest_book(book_list = []):
	suggested_book = random.choice(book_list)
	pages = random.randint(1,2000)
	return suggested_book,pages
def add_books(prompt,book_list = []):
	book_list.append(prompt)
	return book_list
def remove_books(prompt,book = []):
	while prompt in book:
		book.remove(prompt)
	return book
def update_books(prompt1,prompt2,book = []):
	while prompt1 in book:
		book.remove(prompt1)
		book.append(prompt2)
		return book
def show_books(book_list = []):
	return book_list
def welcome_page():
	dash_board = """
		|``````````````````````````|
		| WELCOME TO EMMAX LIBRARY |
		|__________________________|
	"""

	return dash_board
def back():
	back = """
	|```````````````````````````````````````````|
	|    THANK YOU FOR CHOOSING EMMAX LIBRARY   |
	|___________________________________________|
	"""
	return back