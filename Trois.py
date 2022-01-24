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
from player import Player
from game import Game
from time import sleep
from bot import Bot

##############################################################################

##############################################################################
### These are constants for all cards and the decks for the game. ###
### Do not delete ###

### Any additional constant(s) can be added below here ### - This comment should be deleted before submission

### End of constants ###
##############################################################################

##############################################################################
# Here is where the Trois is played.

##############################################################################

# initialise players' hand and game
player = Player(Game.deal_cards())
bot1 = Bot(Game.deal_cards())
bot2 = Bot(Game.deal_cards())
bot3 = Bot(Game.deal_cards())

play_order = [player, bot1, bot2, bot3]

game = Game(play_order, 50) # initialize game with play order and duration

current_turn = 0

game.start_timer()


# play game until winner decided
while game.time_left > 0:

    # current player
    player = game.play_order[current_turn]

    # Display card at top of pile
    print("PILE: " + game.top_pile)

    # play or pick up, and update hand
    # player's turn, so ask for action
    if type(player) == Player:
        print("HAND: " + ' '.join(player.hand))
        play_to_make = input("Enter card(s) to play: ")
        play_to_make = play_to_make.split()

        for card in play_to_make:
            if player.check_playable(game.top_pile, card):
                game.top_pile = card
                player.remove_card(card)
    # bot's turn
    else:
        sleep(3)
        player.decide_play(game.top_pile)


    # if hand is empty, declare winner and exit loop
    game.check_winner(player)
 
    # move on to next player
    if current_turn == 3:
        current_turn = 0
    else:
        current_turn += 1

    
