from src.Output import Output

class TestOutput(Output):

    list_of_test_output = []

    def get_list_of_test_output(self, list_of_test_output):
        self.list_of_test_output = list_of_test_output

    def display(self, message):
        self.list_of_test_output.append(message)
        return self.list_of_test_output
