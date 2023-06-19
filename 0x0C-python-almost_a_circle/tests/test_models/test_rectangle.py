#!/usr/bin/python3
""" test for rectangle class """
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """ testing the Rectangle class """

    def setUp(self):
        "used for each test """
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """ Testing a new rectangle """
        new = Rectangle(2, 2)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 2)

    def test_new_rectangle_2(self):
        """ Testing the new rectangle with all attrs """
        new = Rectangle(1, 3, 2, 5, 4)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 2)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_rectangles(self):
        """ Testing the new rectangles """
        new = Rectangle(2, 2)
        new2 = Rectangle(2, 2)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """ Testing if the Rectangle is a Base instance """
        new = Rectangle(1, 1)
        self.assertEqual(True, isinstance(new, Base))

    def test_incorrect_amount_attrs(self):
        """ Testing error raise with 1 arg passed """
        with self.assertRaises(TypeError):
            new = Rectangle(2)

    def test_incorrect_amount_attrs_1(self):
        """ Testing error raised with no args passed """
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_access_private_attrs(self):
        """  accessing the private attribute """
        new = Rectangle(2, 2)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
        """ accessing a private attribute """
        new = Rectangle(2, 2)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
        """ accessing a private attribute """
        new = Rectangle(2, 2)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        """ Trying to access to a private attribute """
        new = Rectangle(2, 2)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valide_attrs(self):
        """ passing a string value """
        with self.assertRaises(TypeError):
            new = Rectangle("3", 3, 3, 3, 3)

    def test_valide_attrs_2(self):
        """ passing a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(3, "3", 3, 3, 3)

    def test_valide_attrs_3(self):
        """  passing a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(3, 3, "3", 3, 3)

    def test_valide_attrs_4(self):
        """ passing a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(3, 3, 3, "3", 3)

    def test_value_attrs(self):
        """passing invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(0, 1)

    def test_value_attrs_1(self):
        """ pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(2, 0)

    def test_value_attrs_2(self):
        """ passing invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(2, 2, -2)

    def test_value_attrs_3(self):
        """ passing invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """ area method """
        new = Rectangle(5, 6)
        self.assertEqual(new.area(), 30)

    def test_area_2(self):
        """ return value of area method """
        new = Rectangle(3, 3)
        self.assertEqual(new.area(), 4)
        new.width = 5
        self.assertEqual(new.area(), 15)
        new.height = 5
        self.assertEqual(new.area(), 25)

    def test_area_3(self):
        """ return value of area method """
        new = Rectangle(4, 6)
        self.assertEqual(new.area(), 24)
        new2 = Rectangle(10, 10)
        self.assertEqual(new2.area(), 100)

    def test_display(self):
        """ Testing string printed """
        r1 = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Testing the string printed """
        r1 = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.width = 4
        res = "####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Testing the str return value """
        r1 = Rectangle(2, 5, 2, 4)
        res = "[Rectangle] (1) 2/4 - 2/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_2(self):
        """ Testing the str return value """
        r1 = Rectangle(4, 2, 8, 8, 10)
        res = "[Rectangle] (10) 8/8 - 4/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r1.id = 1
        r1.width = 7
        r1.height = 21
        res = "[Rectangle] (1) 8/8 - 7/21\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_3(self):
        """ Testing the str return value """
        r1 = Rectangle(6, 10)
        res = "[Rectangle] (1) 0/0 - 6/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(25, 80, 4, 7)
        res = "[Rectangle] (2) 4/7 - 25/80\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r3 = Rectangle(1, 1, 1, 1)
        res = "[Rectangle] (3) 1/1 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r3)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_4(self):
        """ Testing the str return value """
        r1 = Rectangle(4, 4)
        res = "[Rectangle] (1) 0/0 - 4/4"
        self.assertEqual(r1.__str__(), res)

    def test_display_3(self):
        """ Testing the string printed """
        r1 = Rectangle(4, 4, 1, 1)
        res = "\n ####\n ####\n ####\n ####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_4(self):
        """ Testing string printed """
        r1 = Rectangle(4, 2)
        res = "####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.x = 4
        res = "    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.y = 2
        res = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary(self):
        """ Testing the  dictionary  """
        r1 = Rectangle(1, 2, 3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ Testing dictionary """
        r1 = Rectangle(3, 3, 3, 3)
        res = "[Rectangle] (1) 3/3 - 3/3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(5, 7)
        res = "[Rectangle] (2) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

    def test_dict_to_json(self):
        """ Testing dictionary to JSON string """
        r1 = Rectangle(2, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_check_value(self):
        """ Testing args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-2, 3)

    def test_check_value_2(self):
        """ Testing args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, -3)

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 98}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 98)

    def test_create_2(self):
        """ Test create method """
        dictionary = {'id': 98, 'width': 1}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.width, 1)

    def test_create_3(self):
        """ Testing create method """
        dictionary = {'id': 98, 'width': 1, 'height': 2}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_create_4(self):
        """ Testing create method """
        dictionary = {'id': 98, 'width': 4, 'height': 2, 'x': 3}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_create_5(self):
        """ Testing the create method """
        dictionary = {'id': 98, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_load_from_file(self):
        """ Testing load JSON file """
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, [])

    def test_load_from_file_2(self):
        """ Testing load JSON file """
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        linput = [r1, r2]
        Rectangle.save_to_file(linput)
        loutput = Rectangle.load_from_file()

        for a in range(len(linput)):
            self.assertEqual(linput[a].__str__(), loutput[a]__str__())
