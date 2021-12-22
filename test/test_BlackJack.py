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

    def test_find_winner(self):
        hands = [["SA", "CK", "D4"], ["SA", "CK", "D4"]]
        self.assertEquals(2, len(find_winner(hands)))
        hands = [["SA", "CK", "D5"], ["SA", "CK", "D4"]]
        self.assertEquals(1, len(find_winner(hands)))

    def test_initialise_computer_risk(self):

        # computer_risk would not fall within 2,9 range
        # computer_risk values would not match number_of_players

        number_of_player = 4

        self.assertNotEqual(4, len(list(initialise_computer_risk(number_of_player))))

    def test_valid_deal_input_D(self):

        self.input.set_list_of_test_input(["D", "S"])
        set_game_input(self.input)
        #blackjack using testing input
        self.assertEqual("D", valid_deal_input())