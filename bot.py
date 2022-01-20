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
from game import Game
from player import Player
from constants import PLAYABLE, NOT_PLAYABLE

class Bot(Player):

    def __init__(self):
        super().__init__()

    # choose an optimal action and make the play
    def decide_play(self):
        playable_cards = []
        # check all cards on hand against the topmost card on the pile to 
        # determine if there is/are any playable card(s), and store any 
        # possible playable card(s) in an array
        for i in range(len(self.hand) - 1):
            if Player.check_playable() == PLAYABLE:
                playable_cards.append(self.hand[i])
        
        playable_cards_num = len(playable_cards)
        
        # if there are no playable card(s), then take a random card from 
        # the deck. Otherwise, play the card(s) into the pile from the array
        if playable_cards_num == NOT_PLAYABLE:
            self.pick_card()
        else:
            for _ in range(playable_cards_num - 1):
                self.play_card()
        return
