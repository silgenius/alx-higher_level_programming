import unittest
from models.square import Square

class TestSquareClass(unittest.TestCase):

    def test_square_initialization(self):
        # Test Square initialization with default values
        square1 = Square(5)
        self.assertEqual(square1.size, 5)
        self.assertEqual(square1.width, 5)
        self.assertEqual(square1.height, 5)
        self.assertEqual(square1.x, 0)
        self.assertEqual(square1.y, 0)

        # Test Square initialization with custom values
        square2 = Square(3, 2, 1, 100)
        self.assertEqual(square2.id, 100)
        self.assertEqual(square2.size, 3)
        self.assertEqual(square2.width, 3)
        self.assertEqual(square2.height, 3)
        self.assertEqual(square2.x, 2)
        self.assertEqual(square2.y, 1)

    def test_square_validation(self):
        # Test Square validation with invalid size (less than 1)
        with self.assertRaises(ValueError):
            Square(0)

        # Test Square validation with invalid x and y (less than 0)
        with self.assertRaises(ValueError):
            Square(5, -1, 2)
        with self.assertRaises(ValueError):
            Square(5, 1, -2)

        # Test Square validation with invalid data types
        with self.assertRaises(TypeError):
            Square("invalid")  # Size must be an integer
        with self.assertRaises(TypeError):
            Square(5, "x", 2)  # x must be an integer
        with self.assertRaises(TypeError):
            Square(5, 1, "y")  # y must be an integer

    def test_square_str_method(self):
        # Test Square __str__ method
        square = Square(4, 1, 3, 42)
        self.assertEqual(str(square), "[Square] (42) 1/3 - 4")

class TestSquareUpdateMethod(unittest.TestCase):

    def test_update_with_no_keyword_args(self):
        # Test update with no-keyword arguments
        square = Square(5, 2, 3, 1)
        square.update(10, 20, 30, 40)

        # Check if attributes are updated correctly
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 30)
        self.assertEqual(square.y, 40)

    def test_update_with_keyword_args(self):
        # Test update with keyword arguments
        square = Square(5, 2, 3, 1)
        square.update(id=100, size=200, x=300, y=400)

        # Check if attributes are updated correctly
        self.assertEqual(square.id, 100)
        self.assertEqual(square.size, 200)
        self.assertEqual(square.x, 300)
        self.assertEqual(square.y, 400)

class TestSquareToDictionaryMethod(unittest.TestCase):

    def test_to_dictionary_method(self):
        # Test to_dictionary method
        square = Square(4, 2, 3, 42)
        expected_dict = {'id': 42, 'size': 4, 'x': 2, 'y': 3}

        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_to_dictionary_method_with_different_instance(self):
        # Test to_dictionary method with a different square instance
        square = Square(6, 1, 4, 99)
        expected_dict = {'id': 99, 'size': 6, 'x': 1, 'y': 4}

        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_to_dictionary_method_with_default_values(self):
        # Test to_dictionary method with default values
        square = Square(5)
        expected_dict = {'id': 10, 'size': 5, 'x': 0, 'y': 0}

        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_to_dictionary_method_with_no_input(self):
        # Test to_dictionary method with no input
        square = Square(8, 3, 5, 77)
        square.update()
        expected_dict = {'id': 77, 'size': 8, 'x': 3, 'y': 5}

        self.assertEqual(square.to_dictionary(), expected_dict)
