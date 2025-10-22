import unittest
from Back_to_sender_functions import *

class TestBackToSenderFunction(unittest.TestCase):

	def test_that_get_wage_function_returns_right_allowance(self):
		actual = get_wage(25)
		expected = 9000
		actual_2 = get_wage(50)
		expected_2 = 15000
		actual_3 = get_wage(60)
		expected_3 = 20000
		actual_4 = get_wage(71)
		expected_4 =  40500
		
		self.assertEqual(actual,expected)
		self.assertEqual(actual_2,expected_2)
		self.assertEqual(actual_3,expected_3)
		self.assertEqual(actual_4,expected_4)
	def test_that_get_wage_function_raise_type_error_for_strings(self):
		actual = "Emmax"
		actual_2 = -1  
		self.assertRaises(TypeError,actual)
		self.assertRaises(TypeError,actual_2)
