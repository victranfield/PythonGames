import unittest
from src.TestOutput import TestOutput
from src.TestInput import TestInput


class TestOutputTest(unittest.TestCase):

    output = TestOutput()
    input = TestInput()

    def test_get_string_first(self):

        list_of_test_output = ["Your hand is", "Please select (D)raw or (S)tick:"]
        self.output.get_list_of_test_output(list_of_test_output)

        self.assertEqual(self.output.list_of_test_output[0], "Your hand is")

    def test_get_string_second(self):

        list_of_test_outputs = ["Your hand is", "Please select (D)raw or (S)tick:"]
        self.output.get_list_of_test_output(list_of_test_outputs)

        self.assertEqual(list_of_test_outputs[1], "Please select (D)raw or (S)tick:")


if __name__ == '__main__':
    unittest.main()
