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
from player import Player
from constants import CARDS_IN_HAND, INITIAL_DECK, CARDS_IN_SUIT, SUIT_NUM, \
    CARDS_IN_HAND,  PLAY_DECK, DEAL, PLAY
import bot
from random import randint

class Game:
    
    # initialise wth a list in turn order
    def __init__(self, turn_order):
        self.turn_order = turn_order

        
    # give all players random hands the at start of the game
    @classmethod
    def deal_cards(cls):
        hand = []

        for _ in range(CARDS_IN_HAND):
            card = cls.random_card(DEAL)
            hand.append(card)

        return hand
        
    
    # generates and returns a random card
    @classmethod
    def random_card(cls, generate_type):
        # start of game
        if generate_type == DEAL:
            suit = INITIAL_DECK[randint(0, len(INITIAL_DECK) - 1)]
            card = suit[randint(0, len(suit) - 1)]

        # game progresses
        elif generate_type == PLAY:
            suit = PLAY_DECK[randint(0, len(PLAY_DECK) - 1)]
            card = suit[randint(0, len(suit) - 1)]

        return card

    
    # checks if hand of current player is empty
    def check_winner(player: Player):
        if not player.hand:
            pass
        pass

