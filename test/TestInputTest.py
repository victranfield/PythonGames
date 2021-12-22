import unittest
from src.TestInput import TestInput

class MyTestCase(unittest.TestCase):
    input = TestInput()

    def test_get_string_first(self):

        list_of_test_inputs = ["D", "S"]
        self.input.set_list_of_test_input(list_of_test_inputs)

        self.assertEqual("D", self.input.get_string("S"))

    def test_get_string_second(self):

        list_of_test_inputs = ["D", "S"]
        self.input.set_list_of_test_input(list_of_test_inputs)
        self.input.get_string("S")

        self.assertEqual("S", self.input.get_string("S"))


if __name__ == '__main__':
    unittest.main()
