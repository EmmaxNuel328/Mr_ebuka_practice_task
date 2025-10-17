import unittest
import Transaction_functions


class TestTransactionFunctions(unittest.TestCase):
	def test_that_deposit_function_exist(self):
		Transaction_functions.deposit(1000,0,[200])
	def test_that_withdraw_function_exist(self):
		Transaction_functions.withdraw(1000,0,[200])

		