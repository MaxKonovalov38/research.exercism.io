import unittest
from exercism_step_1 import redacting_str

class EncodeTestCase(unittest.TestCase):
	'''
	Тесты для 'exercism_step_1.py'
	'''

	def test_redact_01(self):
		test_data = redacting_str('HEL LO')
		self.assertEqual(test_data, 'HELLO')

	def test_redact_02(self):
		test_data = redacting_str('M-Y')
		self.assertEqual(test_data, 'MY')

	def test_redact_03(self):
		test_data = redacting_str('Hello, World!')
		self.assertEqual(test_data, 'HelloWorld')


if __name__ == '__main__':
	unittest.main()