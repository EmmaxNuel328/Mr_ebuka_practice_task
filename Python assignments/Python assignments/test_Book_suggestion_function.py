import unittest
import Book_suggestion_function


class TestBookSuggestion(unittest.TestCase):
	def test_that_suggest_book_function_exist(self):
		Book_suggestion_function.suggest_book(1)