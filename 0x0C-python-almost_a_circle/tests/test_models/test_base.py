import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseClass(unittest.TestCase):
    def test_initialization_without_id(self):
        obj = Base(id=None)
        self.assertEqual(obj.id, 2)  # Since __nb_objects is a private attribute starting from 0

    def test_initialization_with_id(self):
        obj_id = 42
        obj = Base(id=obj_id)
        self.assertEqual(obj.id, obj_id)

    def test_multiple_instances(self):
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_id_assignment(self):
        obj = Base()
        obj_id = 10
        obj.id = obj_id
        self.assertEqual(obj.id, obj_id)

class TestBaseToJsonStringMethod(unittest.TestCase):
    def test_to_json_string_method_with_non_empty_list(self):
        # Test to_json_string method with a non-empty list of dictionaries
        list_of_dicts = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_string = Base.to_json_string(list_of_dicts)
        expected_json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'

        self.assertEqual(json_string, expected_json_string)

    def test_to_json_string_method_with_empty_list(self):
        # Test to_json_string method with an empty list
        empty_list = []
        json_string = Base.to_json_string(empty_list)
        expected_json_string = '[]'

        self.assertEqual(json_string, expected_json_string)

    def test_to_json_string_method_with_none(self):
        # Test to_json_string method with None
        json_string = Base.to_json_string(None)
        expected_json_string = '[]'

        self.assertEqual(json_string, expected_json_string)

    def test_to_json_string_method_with_rectangle_instance(self):
        # Test to_json_string method with a single Rectangle instance
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        expected_json_string = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]'

        self.assertEqual(json_string, expected_json_string)

    def test_to_json_string_method_with_square_instance(self):
        # Test to_json_string method with a single Square instance
        s1 = Square(5, 2, 3, 1)
        dictionary = s1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        expected_json_string = '[{"id": 1, "x": 2, "size": 5, "y": 3}]'

        self.assertEqual(json_string, expected_json_string)

    def test_to_json_string_method_with_multiple_instances(self):
        # Test to_json_string method with a mix of Rectangle and Square instances
        r1 = Rectangle(10, 7, 2, 8, 6)
        s1 = Square(5, 2, 3, 1)
        list_of_dicts = [r1.to_dictionary(), s1.to_dictionary()]
        json_string = Base.to_json_string(list_of_dicts)
        expected_json_string = '[{"x": 2, "y": 8, "id": 6, "height": 7, "width": 10},' \
                ' {"id": 1, "x": 2, "size": 5, "y": 3}]'

        self.assertEqual(json_string, expected_json_string)

class TestBaseCreateMethod(unittest.TestCase):

    def test_create_method_with_rectangle(self):
        # Test create method with Rectangle class
        rectangle_dict = {'id': 1, 'width': 10, 'height': 5, 'x': 2, 'y': 3}
        rectangle_instance = Rectangle.create(**rectangle_dict)

        # Check if the instance is of Rectangle class
        self.assertIsInstance(rectangle_instance, Rectangle)

        # Check if attributes are set correctly
        self.assertEqual(rectangle_instance.id, 1)
        self.assertEqual(rectangle_instance.width, 10)
        self.assertEqual(rectangle_instance.height, 5)
        self.assertEqual(rectangle_instance.x, 2)
        self.assertEqual(rectangle_instance.y, 3)

    def test_create_method_with_square(self):
        # Test create method with Square class
        square_dict = {'id': 2, 'size': 7, 'x': 1, 'y': 2}
        square_instance = Square.create(**square_dict)

        # Check if the instance is of Square class
        self.assertIsInstance(square_instance, Square)

        # Check if attributes are set correctly
        self.assertEqual(square_instance.id, 2)
        self.assertEqual(square_instance.size, 7)
        self.assertEqual(square_instance.x, 1)
        self.assertEqual(square_instance.y, 2)

class TestBaseFromJsonStringMethod(unittest.TestCase):

    def test_from_json_string_method_with_non_empty_string(self):
        # Test from_json_string method with a non-empty JSON string
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        list_of_dicts = Base.from_json_string(json_string)

        expected_list = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]

        self.assertEqual(list_of_dicts, expected_list)

    def test_from_json_string_method_with_empty_string(self):
        # Test from_json_string method with an empty JSON string
        empty_json_string = '[]'
        list_of_dicts = Base.from_json_string(empty_json_string)

        expected_list = []

        self.assertEqual(list_of_dicts, expected_list)

    def test_from_json_string_method_with_none(self):
        # Test from_json_string method with None
        list_of_dicts = Base.from_json_string(None)

        expected_list = []

        self.assertEqual(list_of_dicts, expected_list)

    def test_from_json_string_method_with_single_dict(self):
        # Test from_json_string method with a JSON string containing a single dictionary
        json_string = '[{ "id": 89 }]'
        list_of_dicts = Base.from_json_string(json_string)

        expected_list = [{'id': 89}]

        self.assertEqual(list_of_dicts, expected_list)

    def test_from_json_string_method_with_multiple_dicts(self):
        # Test from_json_string method with a JSON string containing multiple dictionaries
        json_string = '[{ "id": 89 }, { "id": 90 }]'
        list_of_dicts = Base.from_json_string(json_string)

        expected_list = [{'id': 89}, {'id': 90}]

        self.assertEqual(list_of_dicts, expected_list)

class TestBaseSaveToFileMethod(unittest.TestCase):

    def test_save_to_file_method_with_rectangles(self):
        # Test save_to_file method with a list of Rectangle instances
        filename = "Rectangle.json"
        rect1 = Rectangle(4, 5)
        rect2 = Rectangle(6, 8)
        list_of_rectangles = [rect1, rect2]

        try:
            Rectangle.save_to_file(list_of_rectangles)
            self.assertTrue(os.path.isfile(filename))

            # Read the content of the file and check if it matches the expected JSON string
            with open(filename, 'r') as file:
                file_content = file.read()
                expected_json_string = '[{"x": 0, "y": 0, "id": 6, "height": 5, "width": 4},' \
                                        ' {"x": 0, "y": 0, "id": 7, "height": 8, "width": 6}]'
                self.assertEqual(file_content, expected_json_string)

        finally:
            # Clean up: Remove the file after the test
            os.remove(filename)

    def test_save_to_file_method_with_squares(self):
        # Test save_to_file method with a list of Square instances
        filename = "Square.json"
        square1 = Square(3)
        square2 = Square(5)
        list_of_squares = [square1, square2]

        try:
            Square.save_to_file(list_of_squares)
            self.assertTrue(os.path.isfile(filename))

            # Read the content of the file and check if it matches the expected JSON string
            with open(filename, 'r') as file:
                file_content = file.read()
                expected_json_string = '[{"id": 7, "x": 0, "size": 3, "y": 0},' \
                                        ' {"id": 8, "x": 0, "size": 5, "y": 0}]'
                self.assertEqual(file_content, expected_json_string)

        finally:
            # Clean up: Remove the file after the test
            os.remove(filename)

    def test_save_to_file_method_with_empty_list(self):
        # Test save_to_file method with an empty list
        filename = "Rectangle.json"
        empty_list = []

        try:
            Rectangle.save_to_file(empty_list)
            self.assertTrue(os.path.isfile(filename))

            # Read the content of the file and check if it matches the expected JSON string
            with open(filename, 'r') as file:
                file_content = file.read()
                expected_json_string = '[]'
                self.assertEqual(file_content, expected_json_string)

        finally:
            # Clean up: Remove the file after the test
            os.remove(filename)
