import random
# import SplendorBaseDeck
from enum import IntEnum, Enum
from typing import List, Optional
import SplendorBaseDeck

# Define Colors
class SuitName(Enum):
    GREEN = "Emerald"
    BLUE  = "Saphire"
    RED   = "Ruby"
    BLACK = "Onyx"
    WHITE = "Diamond"
    # WILD  = "Gold" # TODO: get base working first
class SuitIndex(IntEnum):
    GREEN = 0
    BLUE  = 1
    RED   = 2
    BLACK = 3
    WHITE = 4
    # WILD  = 5

class Level(Enum):
    ONE   = "*"
    TWO   = "**"
    THREE = "***"

class ResourceList:
    def __init__(self, suits: List[SuitIndex], quantity: List[int]):
        # TODO: I believe using the enum will protect against invalid suits, but should check for invalid (e.g. negative) quantities)
        self.list = [0]*len(SuitIndex)
        if suits and quantity: # TODO: This is meant to catch for the default constructor when you just want an empty list
            for i_suit in range(0,len(suits)):
                # TODO: Error checking on inputs
                self.list[suits[i_suit]] = quantity[i_suit]
        else:
            for suit in SuitIndex: # This may not be necessary. Seems like python leaves a lot of things NONE
                self.list[suit] = 0 # How tokens are indexed
    def SuitCount(self, suit: SuitIndex) -> Optional[int]:
        return self.list[suit]
    def SuitAdd(self, suit: SuitIndex, count: int) -> Optional[bool]:
        # To remove, add negative
        self.list[suit] = self.list[suit] + count
        return True # TODO: Any error checking needed (like checking for None?)

    def __str__(self) -> str:
        return f"List {self.list}"
    def __repr__(self) -> str:
        return self.__str__()

class Card:
    def __init__(self, level: Level, vpValue: int, suit: SuitIndex, cost: ResourceList):
        self.level = level # Shows which deck a card goes into. Information only, as cards should never move between decks.
        self.vpValue = vpValue
        self.suit = suit
        self.cost = cost

    def tokensNeeded(self, cards: ResourceList, tokens: ResourceList) -> int :
        # cards and tokens refer to the cards and tokens the player currently has.
        returnCount = 0 # keep track of total cost across all suits
        for suit in SuitIndex:
            if cards.SuitCount(suit) < self.cost.SuitCount(suit):
                if (cards.SuitCount(suit)+tokens.SuitCount(suit)) > self.cost.SuitCount(suit):
                    returnCount = self.cost.SuitCount(suit)-cards.SuitCount(suit) # how many tokens need to be spent
                else:
                    return -1 # card cannot be afforded
        return returnCount
    
    def isAvailable(self, cards: ResourceList, tokens: ResourceList) -> str:
        costToPlayer = self.tokensNeeded(cards, tokens)
        if costToPlayer == 0:
            return f"FREE! :) "
        elif costToPlayer > 0:
            return f"Costs {costToPlayer} Tokens"
        else:
            return f"Not Available"
    
    def __str__(self) -> str:
        return f"Level {self.level} {self.suit.value} gem of {self.vpValue} costing {self.cost}"
        # TODO_Display: players shouldn't need to memorize color indices: have them print out by enumerations
    def __repr__(self) -> str:
        return self.__str__()

class Deck:
    # currently this class is used for both the supply deck(s) AND for the tableu to show the players
    # TODO: consider splitting this into a base deck class and specialized supply and tableu classes
    def __init__(self, name: str):
        self.level1Cards: List[Card] = []
        self.level2Cards: List[Card] = []
        self.level3Cards: List[Card] = []
        # TODO: Probably a better way to handle level of cards via a list indexed by Level(enum)
        self.name = name
    # Note bene: Base deck for the game is initialized in SplendorBaseDeck.py: SetupBaseDeck() -> Deck

    def shuffle(self):
        random.shuffle(self.level1Cards)
        random.shuffle(self.level2Cards)
        random.shuffle(self.level3Cards)
        
    def draw(self, level:Level) -> Optional[Card]:
        # alternative is using a dictionary of lambda functions, or for Python >=3.10: match
        if level == Level.ONE:
            tmpCards = self.level1Cards # mutable, so this is a reference copy (not value copy)
        elif level == Level.TWO:
            tmpCards = self.level2Cards
        elif level == Level.THREE:
            tmpCards = self.level3Cards

        if not tmpCards: # n.b. not tmpCards works because an empty list is False
            print(f"Level {level} deck is empty")
            return None # deck has run out
        else:
            return tmpCards.pop() # this ALSO affects the original object
    
    def addCard(self, Card) -> Optional[bool]:
        if Card is None:
            # print(f"presented with empty card")
            return False
        if Card.level == Level.ONE:
            tmpCards = self.level1Cards # mutable, so this is a reference copy (not value copy)
        elif Card.level == Level.TWO:
            tmpCards = self.level2Cards
        elif Card.level == Level.THREE:
            tmpCards = self.level3Cards
        else:
            # print(f"level not determined")
            return False

        if tmpCards is None: # need 'is None' because an empty list would be false indicating an error condition.
            # print(f"Adding card, but Level {Card.level} deck is None. Not supposed to happen")
            return False
        else:
            tmpCards.append(Card)
        return True
    
    def __len__(self) -> List[int]:
        return [len(self.level1Cards),len(self.level2Cards),len(self.level3Cards)]
    def __str__(self) -> str:
        return f"Deck: {self.name}, Num cards by level: ONE: {len(self.level1Cards)}, TWO: {len(self.level2Cards)}, THREE: {len(self.level3Cards)}"
    # TODO: Option to print full deck for troubleshooting

class Player:
    def __init__(self, name: str):
        self.name = name # sure, why not name the player even though they expire at the end of every game Prestige style.
        self.vpTotal = 0               # Count of victory points. Can only increase. Triggers game end. 
        self.cardList: List[Card] = []     # These are the cards the player currenly has in inventory. Only grows in this game
        self.cardCount  = ResourceList(suits=None, quantity=None) # no limit on cards
        self.tokenCount = ResourceList(suits=None, quantity=None) 
            # These are the tokens gained through mining and spent to get cards. 
        self.TotalTokens = 0           # Total count is limited. 
        
    def draw_card(self, deck: Deck, level: Level) -> Optional[Card]:
        card = deck.draw(level = level)
        if card:
            self.hand.append(card)
            self.cardCount.SuitAdd(card.suit, count=1) # cards always add one jem
            self.vpTotal = self.vpTotal + card.vpValue
        return card # master will need to check if this was a valid draw action via return NONE

    def draw_tokens(self, tokenBank: ResourceList, tokenRequest: ResourceList) -> bool:
        tmpTotalTokens = 0
        tmpDoubleRequested = False
        # The rule: you can take one from three suits or two from one suit (but only if you leave at least two behind)
        for suit in SuitIndex:
            if tokenRequest.SuitCount(suit) == 0:
                pass
                # no tokens requested, go to next suit
            elif tokenRequest.SuitCount(suit) > 2 or tokenRequest.SuitCount(suit) < 0: 
                # cannot request negative tokens bro! Or more than two
                return False
            elif tokenRequest.SuitCount(suit) == 1 and tmpTotalTokens < 3 and not tmpDoubleRequested and tokenBank.SuitCount(suit) >=1:
                tmpTotalTokens = tmpTotalTokens + 1 # True Expression: tmpTotalTokens + tokenRequest.SuitCount(suit)
            elif tokenRequest.SuitCount(suit) == 2 and tmpTotalTokens == 0 and tokenBank.SuitCount(suit) >=4: 
                tmpTotalTokens = 2 # True Expression: tmpTotalTokens + tokenRequest.SuitCount(suit)
                tmpDoubleRequested = True
                # valid so far, move on to next suit (all the others should be zero)
            else:
                return False # something about the request was invalid

        tmpReturn = true
        for suit in SuitIndex:
            tmpReturn = tmpReturn and       tokenBank.SuitAdd(suit,-tokenRequest.SuitCount(suit))
            tmpReturn = tmpReturn and self.tokenCount.SuitAdd(suit, tokenRequest.SuitCount(suit))
            self.TotalTokens = self.TotalTokens + self.tokenCount()
        return tmpReturn # before checks resonable error conditions, so no new failures are expected.

    def __str__(self) -> str:
        return f"Player: {self.name}, Score: {self.vpTotal}, Cards: {len(self.cardList)}, Tokens: {self.TotalTokens}"
        # TODO: print the number of cards by resource.

# # # TODO: 
# Create a method for displaying the full debug state and full and partial play state
# For full play state: 
#    For each player: Basic info (e.g. card / token counts, vpPoints)
#        Print all cards they have (cost not needed) and token totals
# Print the full Tableu: by level, print the <=4 cards including costs
# Print the number of cards in the deck for each level
# For partial play state, for the players just do totals instead of individual cards
# For debug add printing each card in the deck in order
        
# # # Example usage
# # In terminal: 
# import Splendor
# import SplendorBaseDeck
# # deck = Splendor.Deck()
# deck = SplendorBaseDeck.SetupBaseDeck()
# deck.shuffle()
# player = Splendor.Player("Alan")
# card   = Splendor.Card(Splendor.Level.ONE, vpValue=1, suit=Splendor.SuitIndex.GREEN, cost=Splendor.ResourceList(suits=[Splendor.SuitIndex.GREEN, Splendor.SuitIndex.BLUE],quantity=[1,5]))
# card2  = Splendor.Card(Splendor.Level.ONE, vpValue=1, suit=Splendor.SuitIndex.GREEN, cost=Splendor.ResourceList(suits=[],quantity=[]))


# # In program: 
# if __name__ == "__main__":
def demoGame():
    # Create and shuffle a deck
    deck = SplendorBaseDeck.SetupBaseDeck()
    deck.shuffle()
    print(f"Deck: {deck}")
    # Create players
    player1 = Player("Alan") # outside of this file: Splendor.Player(
    player2 = Player("Bobby")
    
    # Create the tableu
    tableu = Deck("Tableu")
    for i_card in range(0,4):
        tableu.addCard(deck.draw(level=Level.ONE))
        tableu.addCard(deck.draw(level=Level.TWO))
        tableu.addCard(deck.draw(level=Level.THREE))
        # Verified that excessive draws do NOT result in undesired behavior 
        # and Do result in a warning
    print(f"Deck:   {deck}")
    print(f"tableu: {tableu}")
    numTokens  = 4 # this is based on player count. TODO: Add a dictionary here which will map player count to number tokens
    # tokenSupply = ResourceList([
    #     (SuitIndex.GREEN,numTokens),
    #     (SuitIndex.BLUE, numTokens),
    #     (SuitIndex.RED,  numTokens),
    #     (SuitIndex.BLACK,numTokens),
    #     (SuitIndex.WHITE,numTokens)])
    tokenSupply = ResourceList([
        SuitIndex.GREEN,
        SuitIndex.BLUE,
        SuitIndex.RED,
        SuitIndex.BLACK,
        SuitIndex.WHITE], [
        numTokens,
        numTokens,
        numTokens,
        numTokens,
        numTokens])
    print(f"tokenSupply: {tokenSupply}")

    # Examples of mining for tokens
    # Valid requests: build up supply
    # Invalid requests: check robustness
    # Examples of buying a card
    #   # Since all turns are hard coded for unit test, should specifically 
    #   # pack the deck so the turns are known valid.
    # show that player attibutes are done correctly

    # # Show current state: Tableu, deck size, players with cards, tokens and victory points
    # # Check for end game trigger
    # # Check for end game

    
    # # Determine winner


    # Nobles are NOT yet implemented
    # Gold / wild is NOT yet implemented