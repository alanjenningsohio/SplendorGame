# SplendorGame
Practice in coding in python by replicating mechanics in the game

# Splendor.py
__Enums__: cards have properties of the suite (e.g. the color of the card bonus: e.g. Emerald) and the Level. The Level is important since each deck only contains cards of the three levels: I, II, and III. Each level going up is more expensive but offers more victory points (e.g. Level I cards have at most 1 victory point while Level 3 can go up to 5 victory points).

__Objects__:
The three main objects are players, the deck and resource lists.
* Players instigate the actions for the game. This controls the mechanisms of the action request. The specifics of the request (e.g. which card to buy) will come as users inputs in the main program.
* The deck controls the card market, such as buying and drawing the cards.
Resource lists are used to tally up and compare costs vs available. This generic term "resource" was choosen to denote that it applies to both lists of cards and tokens.
* Lists are the primary choice to goup similarly typed objects (e.g. the collection of cards a player has is a list).

# SplendorBaseDeck.py
Data file for setting up the contents of the deck
single method: SetupBaseDeck() -> returns a Splendor.Deck object with cards filled with appropriate values (TODO: only a snippet is currently implemented for testing).
