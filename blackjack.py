import random
import itertools


class Deck:
    """
    A class used to represent a deck of cards.
    """

    def __init__(self):
        cards = list(range(2,11)) + ['J', 'Q', 'K', 'A']
        k = 4
        
        # create a deck of cards
        self.cards = list(itertools.chain.from_iterable(itertools.repeat(i, k) for i in cards))


class Player:
    """
    A class used to represent a player in a game of blackjack.

    Attributes:
    -----------
    hand : list
    score : int
    """
    def __init__(self):
        self.hand = []
        self.score = 0

    def use_ace_scoring(self):  # Uses the ace scoring technique defined in the guide
        if self.score + 11 <= 21:
            self.score += 11
        else:
            self.score += 1

    def hit(self, deck):
        """
        Shuffles the deck and gives a card for the user -- could be the dealer or the player

        Parameters:
        -----------
        deck: Deck
        """
        
        random.shuffle(deck.cards)
        new_card = deck.cards.pop()
        self.hand.append(new_card)

        if self.score != 0: 
            self.update_score(new_card)

    def update_score(self, new_card):
        """
        Accepts the new card added to the hand and updates the score.

        Parameters:
        -----------
        new_card: str
        """

        if new_card == "A":
            self.use_ace_scoring()
        elif new_card in {"J", "Q", "K"}:
            self.score += 10
        else: self.score += int(new_card)
        

    def get_hand_value(self):
        """
        Calculates the hand value of the given player.

        Returns:
        ---------
        int
            the score of the hand for the given player
        """
        self.score = 0

        from collections import Counter
        hand_dict = Counter(self.hand)
        
        num_of_a = hand_dict['A']

        for card, freq in hand_dict.items():
            if card in {'J', 'Q', 'K'}: self.score += 10*freq
            elif card != 'A': self.score += int(card)*freq

        while num_of_a:
            self.use_ace_scoring()
            num_of_a -= 1

        return self.score



class Blackjack:
    """
    A class holding the logic for a game of blackjack.
    """
    def __init__(self):
        self.deck = Deck()

    def play_game(self):
        self.dealer = Player()
        self.player = Player()

        for _ in range(2):
            self.dealer.hit(self.deck)
            self.player.hit(self.deck)

        initial_dealer_score = self.dealer.get_hand_value()
        initial_player_score = self.player.get_hand_value()

        # WHile the player hasn't busted, they get the choice to hit or stand
        while self.player.score < 21:
            
            print(f"Dealer has: {' '.join(map(str, self.dealer.hand[:-1]))} ? = ?")
            print(f"Player has: {' '.join(map(str, self.player.hand))} = {self.player.score}")

            player_choice = input("Would you like to (H)it or (S)tand? ")

            if player_choice.lower() == "h" or player_choice.upper() == "hit":
                self.player.hit(self.deck)
            elif player_choice.lower() == "s" or player_choice.upper() == "stand":
                print(f"\nPlayer stands with {' '.join(map(str, self.player.hand))} = {self.player.score}")
                break
            else:
                print("\nPlease enter a valid input!")

        if self.player.score == 21:
            print("\nPlayer wins!")
            print("Blackjack!")
            return

        elif self.player.score > 21:
            print(f"\nPlayer has: {' '.join(map(str, self.player.hand))} = {self.player.score}")
            print(f"Player busts with {self.player.score}")
            return

        else:
            # Dealer's turn: it plays by a simple rule -- hit while the hand value < 17
            while self.dealer.score < 17:
                print("\nDealer hits")
                self.dealer.hit(self.deck)
                print(f"Dealer has: {' '.join(map(str, self.dealer.hand))} = {self.dealer.score}")
            if self.dealer.score > 21:
                print(f"Dealer busts with {' '.join(map(str, self.dealer.hand))} = {self.dealer.score}")
                print("Player wins!")
                return
            else: print("Dealer stands\n")

        # If both the player and dealer stand, the one with the highest score wins
        if self.player.score > self.dealer.score:
            print("Player wins!")
            print(f"{' '.join(map(str, self.player.hand))} = {self.player.score} to Dealer's {' '.join(map(str, self.dealer.hand))} = {self.dealer.score}")
        elif self.player.score < self.dealer.score:
            print("Dealer wins!")
            print(f"{' '.join(map(str, self.dealer.hand))} = {self.dealer.score} to Player's {' '.join(map(str, self.player.hand))} = {self.player.score}")
        else:
            print(f"The game is a tie with a value of {self.player.score} to both the dealer and the player")



if __name__ == '__main__':
    bj = Blackjack()
    bj.play_game()