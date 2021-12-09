from src.Input import Input

class TestInput(Input):

    list_of_test_input = []

    def set_list_of_test_input(self, list_of_test_input):
        self.list_of_test_input = list_of_test_input

    def get_string(self, message):
        return self.list_of_test_input.pop(0)