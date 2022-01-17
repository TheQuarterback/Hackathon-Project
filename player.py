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

class Player:

    def __init__(self, given_hand):
        self.hand = given_hand

    # remove card from hand, returns nothing
    def remove_card(hand, card):
        pass
    
    # add card to hand, returns nothing
    def add_card(hand, card):
        pass

    # play card to pile
    def play_card(self):
        pass
    
    # pick up a card from deck
    def pick_card(self):
        pass

    # check if card is playable
    def check_playable(self, top_pile):
        pass
    