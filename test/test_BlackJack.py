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
        set_game_input(self.input)

    def test_score_hand(self):
        hand = ["SA", "CK", "D4"]
        self.assertEquals(15, score_hand(hand))

    def test_deal_to_player(self):
        # pre conditions
        hand = ["SA", "CK", "D4"]
        deck = ["HA", "S6"]
        self.assertEquals(15, score_hand(hand), "hand is lower than 21 before calling deal_to_player")

        #call the function
        result = deal_to_player(deck, hand)

        #post condition asserts
        self.assertEquals(["HA"], deck, "dealer removed card from deck")
        self.assertEquals(["SA", "CK", "D4", "S6"], hand, "card removed from deck added to hand")
        self.assertEquals(21, score_hand(hand), "value of hand changed to 21, winning value")
        self.assertEquals(True, result, "because it was winning value, return true")


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

    def test_valid_deal_input_Y_S(self):

        self.input.set_list_of_test_input(["Y", "S"])
        set_game_input(self.input)
        # blackjack using testing input
        self.assertEqual("S", valid_deal_input())

    def test_valid_deal_input_s_lower(self):
        self.input.set_list_of_test_input(["Y", "s"])
        set_game_input(self.input)
        # blackjack using testing input
        self.assertEqual("S", valid_deal_input())

    def test_deal_to_user_and_win_21(self):
        # pre conditions

        # to win 21 deck needs to end with a sequence of cards which add up to 21 (cards removed from end of deck)
        deck = ['H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'DA', 'D2', 'D3', 'D4',
         'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10',
         'SJ', 'SQ', 'SK', 'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK', 'HA', 'H4', 'H2', 'H3', 'D5', 'H5', 'H6']
        hand = []
        decisions = ["D", "D", "D", "D", "D", "S"]

        self.input.set_list_of_test_input(decisions)

        # now run function
        deal_to_user(deck, hand)

        # post condition checks
        score = score_hand(hand)
        self.assertEqual(21, score, "when cards drawn from deck add up to 21, score should be 21 (winning score)")
        self.assertEqual([], self.output.list_of_test_output, "confirming that all decisions were used")

