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

import game
from constants import INITIAL_DECK, PLUS_2, PLUS_4, \
    PLAYABLE, NOT_PLAYABLE, DEAL, PLAY

class Player:

    def __init__(self, given_hand):
        self.hand = given_hand

    # remove card from hand, returns nothing
    def remove_card(self, card):
        self.hand.remove(card)
    
    # add card to hand, returns nothing
    def add_card(self, card):
        self.hand.append(card)
    
    # pick up a card from the deck
    def pick_card(self):
        card = game.Game.random_card(PLAY)

        if card in INITIAL_DECK:
            self.add_card(card)
        elif card == PLUS_2:
            self.remove_card(card)
            for _ in range(1):
                new_card = game.Game.random_card(PLAY)
                if new_card == PLUS_2 or new_card == PLUS_4:
                    self.remove_card(new_card)
                else:
                    self.add_card(new_card)
        elif card == PLUS_4:
            self.remove_card(card)
            for _ in range(3):
                new_card = game.Game.random_card(PLAY)
                if new_card == PLUS_2 or new_card == PLUS_4:
                    self.remove_card(new_card)
                else:
                    self.add_card(new_card)
        return

    # check if card is playable - returns 1 if playable and 0 otherwise
    def check_playable(self, top_pile, current_card):
        # need to discuss about this
        if len(current_card) == 2 and (top_pile[0] == current_card[0] or \
            top_pile[1] == current_card[1]):
            return PLAYABLE
        else:
            return NOT_PLAYABLE
