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

        self.assertEquals(faces, ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])

        trentine_small()
        self.assertEquals(faces, ["A", "2", "3", "4", "5", "6", "7", "J", "Q", "K"])

        # 4 cards, 4 players - each player has 1

    def test_deal_cards_one_card_each(self):
        deck = ["1", "2", "3", "4"]

        hands = deal_cards(deck, 1, 4)

        # 4 arrays
        # each array - 1 element
        # first player gets last card

        self.assertEquals(hands, [["4"], ["3"], ["2"], ["1"]])

    def test_deal_cards_two_cards_each(self):
        deck = ["1", "2", "3", "4"]

        hands = deal_cards(deck, 2, 2)

        # 4 arrays
        # each array - 1 element
        # first player gets last card

        self.assertEquals(hands, [["4", "3"], ["2", "1"]])

    def test_play_a_card(self):

        hand = ["1", "2", "3"]

        play_a_card(hand, "3")

        self.assertEquals(hand, ["1", "2"])

    def test_is_playing_a_card(self):

        hand = ["1", "2", "3"]

        self.assert_(is_playing_a_card(hand, "2"))
        self.assertEquals(hand, ["1", "3"])

    def test_is_not_playing_a_card(self):

        hand = ["1", "2", "3"]

        self.assertFalse(is_playing_a_card(hand, "4"))
        self.assertEquals(hand, ["1", "2", "3"])

    def test_convert_face_to_number(self):

        self.assertEquals(convert_face_to_number("S10"), "S10")
        self.assertEquals(convert_face_to_number("CK"), "C13")
        self.assertEquals(convert_face_to_number("S4"), "S04")

    def test_convert_faces_to_numbers(self):

        hand = ["SA", "CK", "D4"]

        convert_faces_to_numbers(hand)

        self.assertEquals(hand, ["S01", "C13", "D04"])

    def test_convert_number_to_face(self):

        self.assertEquals(convert_number_to_face("S10"), "S10")
        self.assertEquals(convert_number_to_face("C13"), "CK")
        self.assertEquals(convert_number_to_face("S04"), "S4")

    def test_convert_numbers_to_faces(self):

        hand = ["S01", "C13", "D04"]

        convert_numbers_to_faces(hand)

        self.assertEquals(hand, ["SA", "CK", "D4"])

    def test_sort_hand(self):
        firsthand = ["SA", "CK"]
        hand = ["SA", "CK"]
        sort_hand(hand)
        self.assertNotEqual(firsthand, hand)

    def test_sort_hands(self):
        firsthand = [["SA", "CK"], ["D4", "CQ"]]
        hands = [["SA", "CK"], ["D4", "CQ"]]
        sort_hands(hands)
        self.assertNotEqual(firsthand, hands)