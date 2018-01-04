# Class Deck: singleton
    # in-deck set class attr
    # played class attr
    # method: play card
    # method: reset deck
# class suit: enum in Py3
# class value: enum in Py3
# class card: suit, value
# class game

from random import choice

SUITS = {"diamonds", "hearts", "clubs", "spades"}
VALUES = {"A": 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 10, "Queen": 10, "King": 10}

class Deck(object):

    def __init__(self):
        self.cards = set()
        self.set_deck()

    def set_deck(self):
        self.cards = set()
        for s in SUITS:
            for v in VALUES:
                self.cards.add(Card(s, v))

    def get_card(self):
        return self.cards.pop()


class Card(object):

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Hand(object):

    def __init__(self):
        self.cards = set()
        self.pts = 0

    def add_card(self, card):
        self.cards.add(card)
        self.pts += VALUES[card.value]

    def get_total(self, hand):
        total = 0
        vals = [VALUES[card.value] for card in self.cards]
        for v in vals:
            total += v
        return total

class Game(object):

    def play(self):

        self._setup()

        while self.dealer_hand.pts < 21 and self.player_hand.pts < 21:
            print "Your total is ", self.player_hand.pts
            print "Dealer total is ", self.dealer_hand.pts
            next = self.get_user_input()

            if next == "hit":
                card = self.deck.get_card()
                print "Card is {} of {}".format(card.value, card.suit)
                self.player_hand.add_card(card)

                if self.dealer_hand.pts < 18:
                    card = self.deck.get_card()
                    print "Dealer gets {} of {}".format(card.value, card.suit)
                    self.dealer_hand.add_card(card)

            elif next == "stand":
                while self.dealer_hand.pts < 18:
                    card = self.deck.get_card()
                    print "Dealer gets {} of {}".format(card.value, card.suit)
                    self.dealer_hand.add_card(card)
                break
            elif next == "quit":
                return


        if self.dealer_hand.pts > 21:
            print "YOU WIN!"
        elif self.player_hand.pts > 21:
            print "YOU BUST! Dealer wins."
        else:
            if self.dealer_hand.pts > self.player_hand.pts:
                print "Dealer wins with ", self.dealer_hand.pts
                return
            print "You win with ", self.player_hand.pts
            return

    def _setup(self):
        self.deck = Deck()
        self.dealer_hand = Hand()
        self.player_hand = Hand()

        for deal in range(2):
            card = self.deck.get_card()
            print "Dealer: {} of {}".format(card.value, card.suit)
            self.dealer_hand.add_card(card)
            card = self.deck.get_card()
            print "Player: {} of {}".format(card.value, card.suit)
            self.player_hand.add_card(card)



    @staticmethod
    def get_user_input():
        options = {'hit', 'stand', 'quit'}
        next_move = ''

        while next_move.lower() not in options:
            print "What would you like to do? (hit, stand, quit)?"
            next_move = raw_input("> ")
            if next_move.lower() not in options:
                print "Sorry, I don't understand."

        return next_move

g = Game()
g.play()
