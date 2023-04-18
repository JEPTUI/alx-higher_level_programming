#!/usr/bin/python3
"""
Defines Unittest for class Square
"""

import unittest
import sys
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Testing square.py
    """

    # Test attributes
    def test_all_attr_given(self):
        """Test all attributes match what's given"""
        sq1 = Square(9, 99, 999, 1000)
        self.assertTrue(sq1.width == 9)
        self.assertTrue(sq1.height == 9)
        self.assertTrue(sq1.size == 9)
        self.assertTrue(sq1.x == 99)
        self.assertTrue(sq1.y == 999)
        self.assertTrue(sq1.id == 1000)

    def test_default_attr(self):
        """Test default attributes are set when not given"""
        sq2 = Square(88)
        self.assertTrue(sq2.width == 88)
        self.assertTrue(sq2.height == 88)
        self.assertTrue(sq2.size == 88)
        self.assertTrue(sq2.x == 0)
        self.assertTrue(sq2.y == 0)
        self.assertTrue(sq2.id is not None)

    def test_attr_validated(self):
        """Test attributes are validated before set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")
            Square([10, 3])
            Square({20, })
            Square({"d": 20})
            Square(None)
            Square((30, 20), 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
            Square(9).size(-9)

    # Test arguments given
    def test_invalid_args(self):
        """Test too many args given throws error"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7)
        """Test too little args given throws error"""
        with self.assertRaises(TypeError):
            Square()
            Square(None)

    # Test defined class
    def test_class(self):
        """Test class created is indeed Rectangle"""
        sq = Square(10)
        self.assertEqual(type(sq), Square)

    # Test methods
    def test_area(self):
        """Test method: area"""
        self.assertEqual(Square(3).area(), 9)
        self.assertEqual(Square(4, 0, 0).area(), 16)

    def test_display(self):
        """Test method: display"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Square(4).display()
            b = bufr.getvalue()
        self.assertEqual(b, '####\n####\n####\n####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Square(3, 1, 2).display()
            b = bufr.getvalue()
        self.assertEqual(b, '\n\n ###\n ###\n ###\n')

    def test_print(self):
        """Test method: __str__"""
        sq = Square(1, 2, 3, 44)
        sq.size = 500
        self.assertEqual(str(sq), '[Square] (44) 2/3 - 500')

    def test_update(self):
        """Test method: update(*args)"""
        sq = Square(1, 2, 3, 4)
        sq.update(10, 10, 10, 10)
        self.assertEqual(str(sq), '[Square] (10) 10/10 - 10')
        sq.update()
        self.assertEqual(str(sq), '[Square] (10) 10/10 - 10')
        sq.update(99)
        self.assertEqual(str(sq), '[Square] (99) 10/10 - 10')
        sq.update(99, 5)
        self.assertEqual(str(sq), '[Square] (99) 10/10 - 5')
        sq.update(44, 55, 1, 2)
        self.assertEqual(str(sq), '[Square] (44) 1/2 - 55')

        """Test method: update(*kwargs)"""
        sq.update(id=88, size=77, nokey=99)
        self.assertEqual(str(sq), '[Square] (88) 1/2 - 77')

    def test_to_dictionary(self):
        """Test method: to_dictionary"""
        sdic = Square(1, 2, 3, 4).to_dictionary()
        self.assertEqual(type(sdic), dict)
        sq2 = Square(10, 10)
        sq2.update(**sdic)
        self.assertEqual(str(sq2), '[Square] (4) 2/3 - 1')
