import random

SUITS = {"Diamonds", "Hearts", "Clubs", "Spades"}
VALUES = {"Ace": 11, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 10, "Queen": 10, "King": 10}

class Deck(object):

    def __init__(self):
        self.cards = []
        self.set_deck()

    def set_deck(self):
        self.cards = []
        for s in SUITS:
            for v in VALUES:
                self.cards.append(Card(s, v))

    def get_card(self):
        return self.cards.pop()


class Card(object):

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

    def get_pts(self):
        return VALUES[self.value]


class Hand(object):

    def __init__(self):
        self.cards = []
        self.pts = []

    def add_card(self, card):
        self.cards.append(card)
        if card.value == 'A':
            self.pts = map(lambda pts: pts + 1, self.pts) + \
                       filter(lambda pts: pts < 22, map(lambda pts: pts + 11, self.pts))
        else:
            self.pts = map(lambda pts: pts + card.get_pts(), self.pts)

        if not self.pts:
            if card.value == "A":
                self.pts.append(1)
            self.pts.append(card.get_pts())


    def get_best_total(self):
        while self.pts and self.pts[-1] > 21:
            self.pts.pop(-1)
        if self.pts:
            return self.pts[-1]
        else:
            return "BUST"

class Game(object):

    def play(self):

        self._setup()

        while self.player_hand.pts[0] < 21:

            print "Your cards are ", self.player_hand.cards
            print "Dealer is showing", self.dealer_hand.cards[1:]
            next = self.get_user_input()

            if next == "hit":
                card = self.deck.get_card()
                print "Card is {} of {}".format(card.value, card.suit)
                self.player_hand.add_card(card)

            elif next == "stand":
                break
            elif next == "quit":
                return

        if self.player_hand.get_best_total() == "BUST":
            print "YOU BUST! Dealer wins."
            return

        # Dealer plays out
        print "Dealer's hand is", self.dealer_hand.cards
        if self.dealer_hand.pts[0] < 18:
            card = self.deck.get_card()
            print "Dealer gets {} of {}".format(card.value, card.suit)
            self.dealer_hand.add_card(card)

        if self.dealer_hand.get_best_total() == "BUST":
            print "YOU WIN!"
        else:
            if self.dealer_hand.get_best_total() > self.player_hand.get_best_total():
                print "Dealer wins with ", self.dealer_hand.get_best_total()
            elif self.dealer_hand.get_best_total() < self.player_hand.get_best_total():
                print "You win with ", self.player_hand.get_best_total()
            else:
                print "It's a push."


    def _setup(self):
        self.deck = Deck()
        random.shuffle(self.deck.cards)
        self.dealer_hand = Hand()
        self.player_hand = Hand()

        for deal in range(2):
            card = self.deck.get_card()
            # print "Dealer: {} of {}".format(card.value, card.suit)
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
