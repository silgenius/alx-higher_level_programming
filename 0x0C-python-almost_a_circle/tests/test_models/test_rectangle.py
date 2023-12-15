import unittest
from models.rectangle import Rectangle
import io
import sys

class TestRectangleClass(unittest.TestCase):
    def test_initialization(self):
        obj = Rectangle(2, 3, 4, 6)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 6)

    def test_initialization_with_other_DataType(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("Bird", 2, 4, 5)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(2, (1, 3), 3, 5)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(2, 2, {"key": 1}, 5)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(2, 3, 8, "y")

    def test_initialization_with_wrong_input(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 7, 6, 5)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(2, 0, 8, 7)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(0, 7, -8, 5)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(2, 0, 8, -1)

    def test_setters_validation(self):
        obj = Rectangle(2, 3, 4, 6)

        with self.assertRaises(TypeError):
            obj.width = "invalid"
        with self.assertRaises(ValueError):
            obj.width = 0

        with self.assertRaises(TypeError):
            obj.height = "invalid"
        with self.assertRaises(ValueError):
            obj.height = 0

        with self.assertRaises(TypeError):
            obj.x = "invalid"
        with self.assertRaises(ValueError):
            obj.x = -1

        with self.assertRaises(TypeError):
            obj.y = "invalid"
        with self.assertRaises(ValueError):
            obj.y = -1

    def test_with_incomplete_arg(self):
        # Test cases for incomplete argument
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, -1, 2)
        
        obj = Rectangle(1, 2, 3)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 0)
        self.assertEqual(obj.id, 13)

        obj = Rectangle(1, 2)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        self.assertEqual(obj.id, 14)

    def test_default_coordinates(self):
        obj = Rectangle(2, 3)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_area(self):
        obj = Rectangle(4, 5)
        self.assertEqual(obj.area(), 20)

    def test_area_args(self):
        with self.assertRaises(TypeError) as x:
            Rectangle(2, 4).area(1)
        self.assertEqual(str(x.exception),
                         "area() takes 1 positional argument but 2 were given")

class TestRectangleDisplay(unittest.TestCase):

    @staticmethod
    def capture_stdout(rect, method):
        capture = io.StringIO()
        sys.stdout = capture
        if method == 'print':
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display_with_args(self):
        with self.assertRaises(TypeError) as x:
            Rectangle(2, 4).display(1)
        self.assertEqual(
            str(x.exception),
            "display() takes 1 positional argument but 2 were given")

    def test_display_with_no_x_no_y(self):
        r = Rectangle(2, 2)
        capture = TestRectangleDisplay.capture_stdout(r, 'display')
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_with_x_no_y(self):
        r = Rectangle(2, 2, 1)
        capture = TestRectangleDisplay.capture_stdout(r, 'display')
        self.assertEqual(" ##\n ##\n", capture.getvalue())

    def test_display_with_no_x_y(self):
        r = Rectangle(2, 2, 0, 1)
        capture = TestRectangleDisplay.capture_stdout(r, 'display')
        self.assertEqual("\n##\n##\n", capture.getvalue())

    def test_display_with_x_y(self):
        r = Rectangle(2, 2, 1, 1)
        capture = TestRectangleDisplay.capture_stdout(r, 'display')
        self.assertEqual("\n ##\n ##\n", capture.getvalue())

class TestRectangleStrMethod(unittest.TestCase):
    def test_str_method(self):
        # Test case with positive x and y
        obj1 = Rectangle(2, 3, 4, 5, 15)
        expected_output1 = "[Rectangle] (15) 4/5 - 2/3"
        self.assertEqual(str(obj1), expected_output1)

        # Test case with x=0 and y=0
        obj2 = Rectangle(2, 3, 0, 0, 6)
        expected_output2 = "[Rectangle] (6) 0/0 - 2/3"
        self.assertEqual(str(obj2), expected_output2)

        # Test case with large width and height
        obj4 = Rectangle(100, 200, 10, 20, 4)
        expected_output4 = "[Rectangle] (4) 10/20 - 100/200"
        self.assertEqual(str(obj4), expected_output4)

        # Test case with id specified
        obj5 = Rectangle(2, 3, 4, 5, 100)
        expected_output5 = "[Rectangle] (100) 4/5 - 2/3"
        self.assertEqual(str(obj5), expected_output5)

class TestRectangleUpdateMethod(unittest.TestCase):
    def test_update_method_with_args(self):
        obj = Rectangle(2, 3, 4, 5)
        obj.update(10, 20, 30, 40, 50)

        # Check if attributes are updated correctly
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 20)
        self.assertEqual(obj.height, 30)
        self.assertEqual(obj.x, 40)
        self.assertEqual(obj.y, 50)

        # Test update with fewer arguments
        obj.update(100, 200, 300)

        # Check if attributes are updated correctly
        self.assertEqual(obj.id, 100)
        self.assertEqual(obj.width, 200)
        self.assertEqual(obj.height, 300)
        # Ensure that x and y are not changed because they were not provided in the update
        self.assertEqual(obj.x, 40)
        self.assertEqual(obj.y, 50)

        # Test update with no arguments
        obj.update()

        # Check if attributes remain the same
        self.assertEqual(obj.id, 100)
        self.assertEqual(obj.width, 200)
        self.assertEqual(obj.height, 300)
        self.assertEqual(obj.x, 40)
        self.assertEqual(obj.y, 50)

    def test_update_method_with_keyword_args(self):
        obj = Rectangle(2, 3, 4, 5)

        # Test update with no-keyword arguments
        obj.update(10, 20, 30, 40, 50)

        # Check if attributes are updated correctly
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 20)
        self.assertEqual(obj.height, 30)
        self.assertEqual(obj.x, 40)
        self.assertEqual(obj.y, 50)

        # Test update with keyword arguments
        obj.update(id=100, width=200, height=300, x=400, y=500)

        # Check if attributes are updated correctly
        self.assertEqual(obj.id, 100)
        self.assertEqual(obj.width, 200)
        self.assertEqual(obj.height, 300)
        self.assertEqual(obj.x, 400)
        self.assertEqual(obj.y, 500)

        # Test update with a mix of both no-keyword and keyword arguments
        obj.update(1000, height=400, x=800)

        # Check if attributes are updated correctly
        self.assertEqual(obj.id, 1000)
        self.assertEqual(obj.width, 200)  # Width remains unchanged
        self.assertEqual(obj.height, 300)
        self.assertEqual(obj.x, 400)
        self.assertEqual(obj.y, 500)  # y remains unchanged

class TestRectangleToDictionaryMethod(unittest.TestCase):

    def test_to_dictionary_method(self):
        # Test to_dictionary method
        rectangle = Rectangle(4, 5, 2, 3, 42)
        expected_dict = {'id': 42, 'width': 4, 'height': 5, 'x': 2, 'y': 3}

        self.assertEqual(rectangle.to_dictionary(), expected_dict)

    def test_to_dictionary_method_with_different_instance(self):
        # Test to_dictionary method with a different rectangle instance
        rectangle = Rectangle(10, 8, 1, 2, 99)
        expected_dict = {'id': 99, 'width': 10, 'height': 8, 'x': 1, 'y': 2}

        self.assertEqual(rectangle.to_dictionary(), expected_dict)

    def test_to_dictionary_method_with_default_values(self):
        # Test to_dictionary method with default values
        rectangle = Rectangle(3, 3)
        expected_dict = {'id': 20, 'width': 3, 'height': 3, 'x': 0, 'y': 0}

        self.assertEqual(rectangle.to_dictionary(), expected_dict)
