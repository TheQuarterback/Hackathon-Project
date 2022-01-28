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

from constants import PLAY
from player import Player
from game import Game
from time import sleep
from bot import Bot
import sys

##############################################################################

##############################################################################
# Here is where the Trois is played.
##############################################################################
# start thegame with simple introductory proses and courtesy
print("Welcome to Trois! A lovely and great game for bored people!")
sleep(1)
print("If this is your first time playing Trois, we recommend reading the",
      "game brochure before starting!")
sleep(1)
player_name = str(input("Enter your name/username: "))
print("Greetings, " + player_name + "!")
print("Bot 1, Bot 2, Bot 3 has joined the game")
sleep(1)
print("Dealer has shuffled and distributed the cards to all players")
sleep(1)
print("Dealer has formed the deck")
sleep(1)
print("Dealer has formed a pile\n")
sleep(1)

# initialise players' hand and game
player = Player(Game.deal_cards())
bot1 = Bot(Game.deal_cards(), 1)
bot2 = Bot(Game.deal_cards(), 2)
bot3 = Bot(Game.deal_cards(), 3)

play_order = [player, bot1, bot2, bot3]

game = Game(play_order, 25) # initialize game with play order and duration in minutes

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

        # check if cards are playable
        cards_to_remove = []
        for card in play_to_make:
            if player.check_playable(game.top_pile, card):
                cards_to_remove.append(card)

        # no cards to play or don't want to play card
        if not cards_to_remove:
            player.pick_card()  
        # update top pile card
        else:
            game.top_pile = cards_to_remove[-1]

        # remove cards
        player.hand = [card for card in player.hand if card not in cards_to_remove]
    # bot's turn
    else:
        sleep(2)
        game.top_pile = player.decide_play(game.top_pile)


    # if hand is empty, declare winner and exit loop
    if game.check_winner(player):
        if current_turn == 0:
            print(f"{player_name} IS THE WINNER!!!")
        else:
            print(f"BOT {current_turn} IS THE WINNER!!!")
        break
 
    # move on to next player
    if current_turn == 3:
        current_turn = 0
    else:
        current_turn += 1

