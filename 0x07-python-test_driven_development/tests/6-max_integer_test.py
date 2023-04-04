#!/usr/bin/python3
""" Unittests for max integer """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Defines unittests for max integer
    """
    def test_empty_list(self):
        """ Test an empty list """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_single_element_list(self):
        """ Test a list with one element """
        single_element = [5]
        self.assertEqual(max_integer(single_element), 5)

    def test_list_with_decimals(self):
        """ Test a list with floating values """
        decimals = [3.5, 6.4, 5.3, 8.5]
        self.assertEqual(max_integer(decimals), 8.5)

    def test_list_with_zero(self):
        """ Tests a list with a value 0 """
        zero_list = [-5, 0, 5, 2]
        self.assertEqual(max_integer(zero_list), 5)

    def test_list_with_mixed_data_types(self):
        with self.assertRaises(TypeError):
            """Tests a list with different data types """
            mixed_list = [1, 2, 'a', 4]
            max_integer(mixed_list)

    def test_ints_and_floats(self):
        """ Tests a list with integers and floats """
        ints_floats = [7, 5.5, 8, 6.5, 9, 7.5]
        self.assertEqual(max_integer(ints_floats), 9)

    def test_ordered_list(self):
        """ Tests an ordered list """
        ordered_list = [4, 5, 6, 7, 8]
        self.assertEqual(max_integer(ordered_list), 8)

    def test_unordered_list(self):
        """ Tests an unordered list """
        unordered_list = [8, 4, 6, 5, 7]
        self.assertEqual(max_integer(unordered_list), 8)

if __name__ == '__main__':
    unittest.main()

