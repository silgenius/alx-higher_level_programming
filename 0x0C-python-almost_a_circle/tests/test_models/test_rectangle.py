import unittest
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    def test_initialization(self):
        obj = Rectangle(2, 3, 4, 6)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 6)

    def test_initialization_with_other_DataType(self):
        self.assertRaises(TypeError, Rectangle, "Bird", 2, 4, 5)
        self.assertRaises(TypeError, Rectangle, 2, (1, 3), 3, 5)
        self.assertRaises(TypeError, Rectangle, 2, 2, {"key": 1}, 5)
        self.assertRaises(TypeError, Rectangle, 2, 3, 8, "y")

    def test_initialization_with_wrong_input(self):
        self.assertRaises(ValueError, Rectangle, 0, 7, 6, 5)
        self.assertRaises(ValueError, Rectangle, 2, 0, 8, 7)
        self.assertRaises(ValueError, Rectangle, 0, 7, -8, 5)
        self.assertRaises(ValueError, Rectangle, 2, 0, 8, -1)

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

    def test_with_no_XorY(self):
        obj = Rectangle(2, 3)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_area(self):
        obj = Rectangle(4, 5)
        self.assertEqual(obj.area(), 20)

class TestRectangleStrMethod(unittest.TestCase):
    def test_str_method(self):
        # Test case with positive x and y
        obj1 = Rectangle(2, 3, 4, 5)
        expected_output1 = "[Rectangle] (1) 4/5 - 2/3"
        self.assertEqual(str(obj1), expected_output1)

        # Test case with x=0 and y=0
        obj2 = Rectangle(2, 3, 0, 0)
        expected_output2 = "[Rectangle] (2) 0/0 - 2/3"
        self.assertEqual(str(obj2), expected_output2)

        # Test case with negative x and y
        obj3 = Rectangle(2, 3, -2, -3)
        expected_output3 = "[Rectangle] (3) -2/-3 - 2/3"
        self.assertEqual(str(obj3), expected_output3)

        # Test case with large width and height
        obj4 = Rectangle(100, 200, 10, 20)
        expected_output4 = "[Rectangle] (4) 10/20 - 100/200"
        self.assertEqual(str(obj4), expected_output4)

        # Test case with id specified
        obj5 = Rectangle(2, 3, 4, 5, 100)
        expected_output5 = "[Rectangle] (100) 4/5 - 2/3"
        self.assertEqual(str(obj5), expected_output5)

class TestRectangleUpdateMethod(unittest.TestCase):
    def test_update_method(self):
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
