import unittest
import Transaction_functions


class TestTransactionFunctions(unittest.TestCase):
	def test_that_deposit_function_exist(self):
		Transaction_functions.suggest_book(1)