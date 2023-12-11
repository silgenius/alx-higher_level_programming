import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    def test_initialization_without_id(self):
        print(f'Before creating instance: {Base._Base__nb_objects}')
        obj = Base(id=None)
        print(f'After creating instance: {Base._Base__nb_objects}')
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
