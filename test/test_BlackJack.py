from unittest import TestCase
from src.BlackJack import *
from src.TestInput import TestInput


class TestBlackJack(TestCase):

    def test_play(self):
        test_input = TestInput()
        test_input.set_list_of_test_input([3,"D","S"])
        set_game_input(test_input)
        main()
