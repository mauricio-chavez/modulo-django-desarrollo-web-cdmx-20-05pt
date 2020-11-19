"""Tests example"""

import unittest
from unittest.mock import MagicMock

from calculator import Calculator


class ExampleTest(unittest.TestCase):
    """Example tests"""

    def setUp(self):
        self.calculator = Calculator()

    def test_add_function(self):
        """Tests that 1 + 1 = 2"""
        result = self.calculator.add(1, 1)
        self.assertEqual(result, 2)

    def test_minus_function(self):
        """Tests that 3 - 2 = 1"""
        result = self.calculator.minus(3, 2)
        self.assertEqual(result, 1)

    def test_multiply_function(self):
        """Tests that 3 by 2 equals what returns add"""
        self.calculator.add = MagicMock(return_value=8)
        result = self.calculator.multiply(3, 2)
        self.assertEqual(result, 8)

    def test_add_and_multiply(self):
        """Tests that 3 by 2 equals 6"""
        result = self.calculator.multiply(3, 2)
        self.assertEqual(result, 6)


unittest.main()
