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

import player
import constants
import bot

class Game:
    
    # initialise wth a list in turn order
    def __init__(self, turn_order):
        self.turn_order = turn_order

    # give all players random hands
    def deal_cards():
        pass
    
    # generates and returns a random card
    def random_card():
        pass

    # checks if hand of current player is empty
    def check_winner():
        pass

