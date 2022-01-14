##############################################################################
# Trois is a modified version of the world-renowned game, Uno, that is jointly
# developed by Anthony Lua and Wui Herng Moo Yong as part of a Hackathon
# project. Trois is a one-player game against three desicion-making bots, and
# the goal of Trois is to get rid of all your cards before the time limit or
# to have the least number fo cards by the time limit. Instructions on how to
# play Trois will be on the READ.ME.md file. We hope that you will enjoy
# playing Trois! Thank you!

# Date (dd/mm/yyyy) of Authorship delcaration for Anthony Lua: 14/01/2022
# Date (dd/mm/yyyy) of Authorship delcaration for Wui Herng Moo Yong:
##############################################################################

##############################################################################
### Libraries used for the game. Additional libraries can be added ###
import random
##############################################################################

##############################################################################
### These are constants for all cards and the decks for the game. ###
### Do not delete ###
ALL_COLOUR_CODE = "BGYPORM"
ALL_NUM = "0123456789"
BLUE_CODE = "B"
GREEN_CODE = "G"
YELLOW_CODE = "Y"
PURPLE_CODE = "P"
ORANGE_CODE = "O"
RED_CODE = "R"
MAGENTA_CODE = "M"
ZERO = "0"
ONE = "1"
TWO = "2"
THREE = "3"
FOUR = "4"
FIVE = "5"
SIX = "6"
SEVEN = "7"
EIGHT = "8"
NINE = "9"
WILDCARD_CODE = "+"
BLUE_0 = "B0"
BLUE_1 = "B1"
BLUE_2 = "B2"
BLUE_3 = "B3"
BLUE_4 = "B4"
BLUE_5 = "B5"
BLUE_6 = "B6"
BLUE_7 = "B7"
BLUE_8 = "B8"
BLUE_9 = "B9"
GREEN_0 = "G0"
GREEN_1 = "G1"
GREEN_2 = "G2"
GREEN_3 = "G3"
GREEN_4 = "G4"
GREEN_5 = "G5"
GREEN_6 = "G6"
GREEN_7 = "G7"
GREEN_8 = "G8"
GREEN_9 = "G9"
YELLOW_0 = "Y0"
YELLOW_1 = "Y1"
YELLOW_2 = "Y2"
YELLOW_3 = "Y3"
YELLOW_4 = "Y4"
YELLOW_5 = "Y5"
YELLOW_6 = "Y6"
YELLOW_7 = "Y7"
YELLOW_8 = "Y8"
YELLOW_9 = "Y9"
PURPLE_0 = "P0"
PURPLE_1 = "P1"
PURPLE_2 = "P2"
PURPLE_3 = "P3"
PURPLE_4 = "P4"
PURPLE_5 = "P5"
PURPLE_6 = "P6"
PURPLE_7 = "P7"
PURPLE_8 = "P8"
PURPLE_9 = "P9"
ORANGE_0 = "O0"
ORANGE_1 = "O1"
ORANGE_2 = "O2"
ORANGE_3 = "O3"
ORANGE_4 = "O4"
ORANGE_5 = "O5"
ORANGE_6 = "O6"
ORANGE_7 = "O7"
ORANGE_8 = "O8"
ORANGE_9 = "O9"
RED_0 = "R0"
RED_1 = "R1"
RED_2 = "R2"
RED_3 = "R3"
RED_4 = "R4"
RED_5 = "R5"
RED_6 = "R6"
RED_7 = "R7"
RED_8 = "R8"
RED_9 = "R9"
MAGENTA_0 = "M0"
MAGENTA_1 = "M1"
MAGENTA_2 = "M2"
MAGENTA_3 = "M3"
MAGENTA_4 = "M4"
MAGENTA_5 = "M5"
MAGENTA_6 = "M6"
MAGENTA_7 = "M7"
MAGENTA_8 = "M8"
MAGENTA_9 = "M9"
PLUS_2 = "+2"
PLUS_4 = "+4"

# *Note that this deck is to be used only at the start of the game.*
INITIAL_DECK = [BLUE_0, BLUE_1, BLUE_2, BLUE_3, BLUE_4, BLUE_5, BLUE_6, \
                BLUE_7, BLUE_8, BLUE_9, GREEN_0, GREEN_1, GREEN_2, GREEN_3, \
                GREEN_4, GREEN_5, GREEN_6, GREEN_7, GREEN_8, GREEN_9, \
                YELLOW_0, YELLOW_1, YELLOW_2, YELLOW_3, YELLOW_4, YELLOW_5, \
                YELLOW_6, YELLOW_7, YELLOW_8, YELLOW_9, PURPLE_0, PURPLE_1, \
                PURPLE_2, PURPLE_3, PURPLE_4, PURPLE_5, PURPLE_6, PURPLE_7, \
                PURPLE_8, PURPLE_9, ORANGE_0, ORANGE_1, ORANGE_2, ORANGE_3, \
                ORANGE_4, ORANGE_5, ORANGE_6, ORANGE_7, ORANGE_8, ORANGE_9, \
                RED_0, RED_1, RED_2, RED_3, RED_4, RED_5, RED_6, RED_7, \
                RED_8, RED_9, MAGENTA_0, MAGENTA_1, MAGENTA_2, MAGENTA_3, \
                MAGENTA_4, MAGENTA_5, MAGENTA_6, MAGENTA_7, MAGENTA_8, \
                MAGENTA_9]

# *Note that this deck is to be used throughtout the game.*
PLAY_DECK = [BLUE_0, BLUE_1, BLUE_2, BLUE_3, BLUE_4, BLUE_5, BLUE_6, \
                BLUE_7, BLUE_8, BLUE_9, GREEN_0, GREEN_1, GREEN_2, GREEN_3, \
                GREEN_4, GREEN_5, GREEN_6, GREEN_7, GREEN_8, GREEN_9, \
                YELLOW_0, YELLOW_1, YELLOW_2, YELLOW_3, YELLOW_4, YELLOW_5, \
                YELLOW_6, YELLOW_7, YELLOW_8, YELLOW_9, PURPLE_0, PURPLE_1, \
                PURPLE_2, PURPLE_3, PURPLE_4, PURPLE_5, PURPLE_6, PURPLE_7, \
                PURPLE_8, PURPLE_9, ORANGE_0, ORANGE_1, ORANGE_2, ORANGE_3, \
                ORANGE_4, ORANGE_5, ORANGE_6, ORANGE_7, ORANGE_8, ORANGE_9, \
                RED_0, RED_1, RED_2, RED_3, RED_4, RED_5, RED_6, RED_7, \
                RED_8, RED_9, MAGENTA_0, MAGENTA_1, MAGENTA_2, MAGENTA_3, \
                MAGENTA_4, MAGENTA_5, MAGENTA_6, MAGENTA_7, MAGENTA_8, \
                MAGENTA_9, PLUS_2, PLUS_4]

WILDCARD_DECK = [PLUS_2, PLUS_4]

### Any additional constant(s) can be added below here ### - This comment should be deleted before submission

### End of constants ###
##############################################################################

##############################################################################
# Here is where the Trois is played.

##############################################################################