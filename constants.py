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

##############################################################################
### These are constants for all cards and the decks for the game. ###
### Do not delete ###


ALL_COLOURS = "BGYPORM"
ALL_NUM = "0123456789"
PLUS_2 ="+2"
PLUS_4 ="+4"
WILDCARDS = [PLUS_2, PLUS_4]

CARDS_IN_HAND = 8

# review 

BLUE_SUIT = ["B0","B1","B2","B3","B4","B5","B6","B7","B8","B9"]
RED_SUIT = ["R0","R1","R2","R3","R4","R5","R6","R7","R8","R9"]
YELLOW_SUIT = ["Y0","Y1","Y2","Y3","Y4","Y5","Y6","Y7","Y8","Y9"]
GREEN_SUIT = ["G0","G1","G2","G3","G4","G5","G6","G7","G8","G9"]
ORANGE_SUIT = ["O0","O1","O2","O3","O4","O5","O6","O7","O8","O9"]
PURPLE_SUIT = ["P0","P1","P2","P3","P4","P5","P6","P7","P8","P9"]
MAGENTA_SUIT = ["M0","M1","M2","M3","M4","M5","M6","M7","M8","M9"]

SUIT_NUM = 7
CARDS_IN_SUIT = 10

INITIAL_DECK = [BLUE_SUIT, RED_SUIT,YELLOW_SUIT,GREEN_SUIT,ORANGE_SUIT,
                PURPLE_SUIT,MAGENTA_SUIT]

PLAY_DECK = INITIAL_DECK + WILDCARDS

# card generation types
DEAL = "Deal"
PLAY = "Play"