import unittest
import Book_suggestion_function


class TestBookSuggestion(unittest.TestCase):
	def test_that_suggest_book_function_exist(self):
		Book_suggestion_function.suggest_book("suggested_book")
	def test_suggest_book_returns_book(self):
		
	def test_that_add_books_function_exist(self):
		Book_suggestion_function.add_books("prompt,book_list = []")
	def test_that_remove_books_function_exist(self):
		Book_suggestion_function.remove_books("prompt,book_list = []")
	def test_that_update_books_function_exist(self):
		Book_suggestion_function.update_books("prompt,book_list = []","Emmax")
	def test_that_show_books_function_exist(self):
		Book_suggestion_function.show_books("Naruto")
	def test_that_show_books_function_exist(self):
		Book_suggestion_function.show_books("Naruto")
	def test_that_welcome_page_function_exist(self):
		Book_suggestion_function.welcome_page()
	def test_that_back_function_exist(self):
		Book_suggestion_function.back()
