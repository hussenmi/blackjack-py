import unittest
import blackjack


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = blackjack.Deck()
        self.dealer = blackjack.Player()
        self.player = blackjack.Player()

    def test_deck_length(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_deck_length_after_first_deal(self):
        for _ in range(2):
            self.dealer.hit(self.deck)
            self.player.hit(self.deck)

        self.assertEqual(len(self.deck.cards), 48)


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.deck = blackjack.Deck()
        self.player = blackjack.Player()

    def test_player_hand(self):
        self.player.hit(self.deck)
        self.assertEqual(len(self.player.hand), 1)

    def test_player_hand_score_with_ace_one(self):
        self.player.hand.append('K')
        self.player.hand.append('4')
        self.player.hand.append('A')
        self.assertEqual(self.player.get_hand_value(), 15)

    def test_player_hand_score_ace_two(self):
        self.player.hand.append('8')
        self.player.hand.append('A')
        self.player.hand.append('A')
        self.assertEqual(self.player.get_hand_value(), 20)


if __name__ == "__main__":
    unittest.main()