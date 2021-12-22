import unittest
from src.PlayingCard import *

class PlayingCardTest(unittest.TestCase):

    def test_generate_deck(self):
        self.assertEqual(52, len(generate_deck()))

    def test_shuffle_cards(self):
        self.assertNotEqual(shuffle_cards(generate_deck()),
                            shuffle_cards(generate_deck()))

    def test_deal_a_card(self):
        self.assertEquals('D6', deal_a_card(['S4', 'C9', 'D6']))

    def test_trentine_small(self):
        # new_card = PlayingCard()

        self.assertEquals(faces, ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])

        trentine_small()
        self.assertEquals(faces, ["A", "2", "3", "4", "5", "6", "7", "J", "Q", "K"])

        # 4 cards, 4 players - each player has 1

    def test_deal_cards_one_card_each(self):
        deck = ["1", "2", "3", "4"]

        # new_card = PlayingCard()

        hands = deal_cards(deck, 1, 4)

        # 4 arrays
        # each array - 1 element
        # first player gets last card

        self.assertEquals(hands, [["4"], ["3"], ["2"], ["1"]])

    def test_deal_cards_two_cards_each(self):
        deck = ["1", "2", "3", "4"]

        # new_card = PlayingCard()

        hands = deal_cards(deck, 2, 2)

        # 4 arrays
        # each array - 1 element
        # first player gets last card

        self.assertEquals(hands, [["4", "3"], ["2", "1"]])

    def test_play_a_card(self):
        # new_card = PlayingCard()

        hand = ["1", "2", "3"]

        play_a_card(hand, "3")

        self.assertEquals(hand, ["1", "2"])

    def test_is_playing_a_card(self):
        # new_card = PlayingCard()

        hand = ["1", "2", "3"]

        self.assert_(is_playing_a_card(hand, "2"))
        self.assertEquals(hand, ["1", "3"])

    def test_is_not_playing_a_card(self):
        # new_card = PlayingCard()

        hand = ["1", "2", "3"]

        self.assertFalse(is_playing_a_card(hand, "4"))
        self.assertEquals(hand, ["1", "2", "3"])