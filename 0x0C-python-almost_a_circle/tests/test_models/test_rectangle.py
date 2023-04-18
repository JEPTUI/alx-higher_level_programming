#!/usr/bin/python3
"""
Defines Unittest for Rectangle class
"""

from io import StringIO
import sys
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Unittest for rectangle.py
    """

    # Test attributes
    def test_all_attr_given(self):
        """Test assigning arguments to givent attributes"""
        rect1 = Rectangle(5, 10, 1, 2, 99)
        self.assertTrue(rect1.width == 5)
        self.assertTrue(rect1.height == 10)
        self.assertTrue(rect1.x == 1)
        self.assertTrue(rect1.y == 2)
        self.assertTrue(rect1.id == 99)

    def test_default_attr(self):
        """Test assigning default attributes when not given"""
        rect2 = Rectangle(5, 6)
        self.assertTrue(rect2.width == 5)
        self.assertTrue(rect2.height == 6)
        self.assertTrue(rect2.x == 0)
        self.assertTrue(rect2.y == 0)
        self.assertTrue(rect2.id is not None)

    def test_attr_validated(self):
        """Test attributes are validated before assigning"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 1, 1, 1, 1)
            Rectangle([10, 3], 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {20, }, 1, 1, 1)
            Rectangle(1, {"d": 20}, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, None, 1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, (30, 20), 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -20, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 1, -99, 1)

    def test_private_attr_access(self):
        """Test accessing private attributes"""
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    # Test given arguments
    def test_invalid_args(self):
        """Test too many args raises error"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)
        """Test too few args raises error"""
        with self.assertRaises(TypeError):
            Rectangle(1)
            Rectangle()
            Rectangle(None)

    # Test class defined
    def test_class(self):
        """Test created class is class  Rectangle"""
        self.assertEqual(type(Rectangle(1, 2)), Rectangle)

    # Test methods
    def test_area(self):
        """Test method: area"""
        self.assertEqual(Rectangle(3, 4).area(), 12)
        self.assertEqual(Rectangle(8, 7, 0, 0).area(), 56)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display(self):
        """Test method: display"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3).display()
            b = bufr.getvalue()
        self.assertEqual(b, '#####\n#####\n#####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3, 1, 2).display()
            b = bufr.getvalue()
        self.assertEqual(b, '\n\n #####\n #####\n #####\n')

    def test_print(self):
        """Test method: __str__"""
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rect), '[Rectangle] (5) 3/4 - 1/2')

    def test_update(self):
        """Test method: update(*args)"""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 10, 10, 10, 10)
        self.assertEqual(str(rect), '[Rectangle] (10) 10/10 - 10/10')
        rect.update()
        self.assertEqual(str(rect), '[Rectangle] (10) 10/10 - 10/10')
        rect.update(99)
        self.assertEqual(str(rect), '[Rectangle] (99) 10/10 - 10/10')
        rect.update(99, 1)
        self.assertEqual(str(rect), '[Rectangle] (99) 10/10 - 1/10')
        rect.update(99, 1, 2)
        self.assertEqual(str(rect), '[Rectangle] (99) 10/10 - 1/2')
        rect.update(99, 1, 2, 3, 4)
        self.assertEqual(str(rect), '[Rectangle] (99) 3/4 - 1/2')

        """Test invalid *args"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect.update(99, 1, 2, 3, "string")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect.update(99, 1, 2, 3, -99)

        """Test method: update(*kwargs)"""
        rect.update(id=55)
        self.assertEqual(str(rect), '[Rectangle] (55) 3/4 - 1/2')
        rect.update(id=44, x=770, y=880, width=990)
        self.assertEqual(str(rect), '[Rectangle] (44) 770/880 - 990/2')
        """Test mixture of valid and invalid *kwargs"""
        rect.update(nokey=1000, invalid=2000, testing=3000, id=4000)
        self.assertEqual(str(rect), '[Rectangle] (4000) 770/880 - 990/2')

    def test_to_dictionary(self):
        """Test method: to_dictionary"""
        rdic = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertEqual(type(rdic), dict)
        rect2 = Rectangle(10, 10)
        rect2.update(**rdic)
        self.assertEqual(str(rect2), '[Rectangle] (5) 3/4 - 1/2')


if __name__ == "__main__":
    unittest.main()
