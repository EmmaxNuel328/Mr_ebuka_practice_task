import unittest
import Transaction_functions
class Test_Transactionfunctions(unittest.TestCase):
	def test_that_deposit_function_exist(self):
		Transaction_functions.deposit(2500,2500)	
