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
