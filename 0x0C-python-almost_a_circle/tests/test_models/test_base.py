#!/usr/bin/python3
""" test for Base class """
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    """ testing the Base class """

    def setUp(self):
        """ Method used for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Testing the assigned id """
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """ Testing the default id """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        """ Testing the nb object attribute """
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
        """ Testing the nb object attributes and assigned id """
        new = Base()
        new2 = Base(1027)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1027)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        """ Testing the string id """
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
        """ Testing for more args to init method """
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        """ accessing the private attributes """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_1(self):
        """ Testing the JSON file """
        Square.save_to_file(None)
        ress = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), ress)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Testing the JSON file """
        Rectangle.save_to_file(None)
        ress = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), ress)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
