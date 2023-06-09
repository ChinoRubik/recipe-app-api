"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers togueter"""

        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """Test substractring numbers"""
        res = calc.substract(15, 10)
        self.assertEqual(res, 5)
