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

from time import sleep
from sys import exit
import threading
from constants import CARDS_IN_HAND, INITIAL_DECK,  \
    CARDS_IN_HAND,  PLAY_DECK, DEAL, PLAY
from random import randint
from player import Player

class Game:
    
    # initialise wth a list in turn order
    def __init__(self, play_order, time_limit = 10):
        self.play_order = play_order
        self.top_pile = Game.random_card(DEAL)
        self.time_left = time_limit

    # start timer
    def start_timer(self):
        self.countdown = threading.Thread(target = self.time_limit)
        self.countdown.start()

    # timer  
    def time_limit(self):

        for t in range(self.time_left):
            self.time_left -= 1
            sleep(1)

        print("\nTIME IS UP!!!\n")
        exit()

        
    # give all players random hands the at start of the game
    @classmethod
    def deal_cards(cls):
        hand = []

        for _ in range(CARDS_IN_HAND):
            card = cls.random_card(DEAL)
            hand.append(card)

        return hand
        
    
    # generates and returns a random card, talk about this in meeting
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
    # declares winner if empty
    def check_winner(self, player: Player):
        if not player.hand:
            print("WINNER!!!")
            exit() # end the program



