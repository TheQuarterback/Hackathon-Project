##############################################################################
# Trois is a modified version of the world-renowned game, Uno, that is jointly
# developed by Anthony Lua and Wui Herng Moo Yong as part of a Hackathon
# project. Trois is a one-player game against three desicion-making bots, and
# the goal of Trois is to get rid of all your cards before the time limit or
# to have the least number fo cards by the time limit. Instructions on how to
# play Trois will be on the READ.ME.md file. We hope that you will enjoy
# playing Trois! Thank you!

# Date (dd/mm/yyyy) of Authorship delcaration for Anthony Lua: 14/01/2022
# Date (dd/mm/yyyy) of Authorship delcaration for Wei Herng Moo Yong: 16/01/2022
##############################################################################

from constants import INITIAL_DECK, PLAY_DECK, PLUS_2, PLUS_4, PLAY_DECK, \
    PLAYABLE, NOT_PLAYABLE
from random import randint


class Player:

    def __init__(self, given_hand):
        self.hand = given_hand

    # remove card from hand, returns nothing
    def remove_card(hand, card):
        hand.remove(card)

    
    # add card to hand, returns nothing
    def add_card(hand, card):
        hand.append(card)
    
    # pick up a card from the deck
    def pick_card(self):
        suit = PLAY_DECK[randint(0, len(PLAY_DECK) - 1)]
        card = suit[randint(0, len(suit) - 1)]

        if card in INITIAL_DECK:
            self.add_card(self.hand, card)
        elif card == PLUS_2:
            self.remove_card(self.hand, card)
            for _ in range(1):
                new_suit = PLAY_DECK[randint(0, len(PLAY_DECK) - 1)]
                new_card = suit[randint(0, len(new_suit) - 1)]
                if new_card == PLUS_2 or new_card == PLUS_4:
                    self.remove_card(self.hand, new_card)
                else:
                    self.add_card(self.hand, new_card)
        elif card == PLUS_4:
            self.remove_card(self.hand, card)
            for _ in range(3):
                new_suit = PLAY_DECK[randint(0, len(PLAY_DECK) - 1)]
                new_card = suit[randint(0, len(new_suit) - 1)]
                if new_card == PLUS_2 or new_card == PLUS_4:
                    self.remove_card(self.hand, new_card)
                else:
                    self.add_card(self.hand, new_card)
        return

    # check if card is playable - returns 1 if playable and 0 otherwise
    def check_playable(self, top_pile, current_card):
        # need to discuss about this
        if top_pile[0] == current_card[0] or top_pile[1] == current_card[1] and \
            len(current_card) == 2:
            return PLAYABLE
        else:
            return NOT_PLAYABLE
