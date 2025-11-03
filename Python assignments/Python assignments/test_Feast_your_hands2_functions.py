import unittest
from Feast_your_hands2_functions import *

class TestFeastYourHands2Functions(unittest.TestCase):
	def test_that_convert_to_integer_convert_string_to_integer(self):
		my_list = ["1","2","3"]
		actual = convert_to_integer(my_list)
		expected = [1,2,3]
		self.assertEqual(actual,expected)