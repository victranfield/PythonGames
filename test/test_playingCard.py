import unittest
from src.PlayingCard import *

class PlayingCardTest(unittest.TestCase):

    def test_generate_deck(self):
        self.assertEqual(52, len(generate_deck()))
