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

class Bot(Player):

    def __init__(self):
        super().__init__()

    # choose an optimal action and make the play
    def decide_play(self):
        pass
