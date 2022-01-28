# Hackathon-Project by Team MelbGridiron (Trois)

*Important note*:

To start the game, download all files and run Trois.py

About:
1. It is a slightly different version of Uno:
- There are more card combinations
- Wildcards work slightly differently
2. It is great for bored people to play
3. One human player plays against three bots
4. The game ends when a character wins by either of the following:
- Having the least number of cards after the time limit (25 minutes) - If two or more characters have the same least number of cards, a tie will be announced
- Having no cards left on hand


Characters in the game:
1. Player (Human)
2. Bot 1
3. Bot 2
4. Bot 3
5. Dealer - Does not play the game (Game engine)


Terminology:
1. Character: A player in the game whether it is human or a bot
2. Deck: These are cards facing downwards
3. Hand: These are the cards a character currently holds
4. Play: This the part where a character has to either put card(s) onto the deck or take a card from the pile
5. Pile: These are cards facing upwards
6. Wildcard pile: This is where wildcards are discarded


Play progression:
1. The dealer opens by taking handing eight random cards (excluding wildcards) from the deck to each character
2. The dealer then takes a card from the deck and place the card facing upwards to create a pile
3. Afterwards, Player and the bots will play the game until one character wins


Rules:
1. Player always start the game
2. Every character starts with 8 cards in hand at the start of the game
3. No character can see each other’s cards
4. The time limit is 25 minutes
5. No wildcards can be given at the start of the game
6. Wildcards can only be obtained from the deck and the character who gets the wildcard must:
- Take two additional cards from the deck if the wildcard is a +2
- Take four additional cards from the deck if the wildcard is a +4
7. Wildcards are to be discarded into the wildcard pile immediately after obtaining them
8. In a play, a character can place card(s) from their hand onto the pile if they match the topmost card on the pile:
- If there is not a single card that can be discarded from their hand onto the pile, they will have to take a card from the deck and then it will be the next character’s turn
9. Matching card(s) is/are of the same colour or number:
- Example of same-colour combination if the topmost card on the pile is blue (B7): [B0, B3, B8], [B6]
- Example of same-number combination if the topmost card on the pile is blue (B7): [G7, P7], [O7]

All game cards:
- Blue: B0, B1, B2, B3, B4, B5, B6, B7, B8, B9

- Green: G0, G1, G2, G3, G4, G5, G6, G7, G8, G9

- Yellow: Y0, Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9

- Purple: P0, P1, P2, P3, P4, P5, P6, P7, P8, P9

- Orange: O0, O1, O2, O3, O4, O5, O6, O7, O8, O9

- Red: R0, R1, R2, R3, R4, R5, R6, R7, R8, R9

- Magenta: M0, M1, M2, M3, M4, M5, M6, M7, M8, M9

- Wildcards: +2, +4
