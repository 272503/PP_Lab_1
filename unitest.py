from main import *
import unittest

class TestStringMethods(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(Add(""), 0)

    def test_add_one_num(self):
        self.assertEqual(Add("1"), 1)

    def test_add_two_nums(self):
        self.assertEqual(Add("1, 2"), 3)

    def test_add_three_nums(self):
        self.assertEqual(Add("1, 2, 3"), 6)

    def test_add_with_enter_two_nums(self):
        self.assertEqual(Add("1\n2"), 3)

    def test_add_with_enter_three_nums(self):
        self.assertEqual(Add("1\n2,3"), 6)

    def test_add_with_enter_four_nums(self):
        self.assertEqual(Add("1\n2\n,5"), "error")

    def test_add_with_enter_bad_data(self):
        self.assertEqual(Add("\n,3\n4,5,"), "error")

