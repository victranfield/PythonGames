from unittest import TestCase
from src.BlackJack import *
from src.TestInput import TestInput
from src.TestOutput import TestOutput

class TestBlackJack(TestCase):

    def test_play(self):
        test_input = TestInput()
        test_input.set_list_of_test_input([3,"D","S"])
        set_game_input(test_input)
        main()

    def setUp(self):
        self.input = TestInput()
        self.output = TestOutput()

    def test_score_hand(self):
        hand = ["SA", "CK", "D4"]
        self.assertEquals(15, score_hand(hand))

    def test_deal_to_player(self):
        hand = ["SA", "CK", "D4"]
        # 15
        # king of clubs
        # draws king
        deck = ["HA", "S6"]
        # exactly 21
        self.assertEquals(True, deal_to_player(deck, hand))
