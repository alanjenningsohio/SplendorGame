import Splendor
# OBSOLETE: rather then adding directly to the list, a method was added so that the input could be error checked (Was adding NONE). 


def SetupBaseDeck() -> Splendor.Deck: 
    deck = Splendor.Deck("MainDeck")
    # level 1
    deck.level1Cards.append(Splendor.Card(level = Splendor.Level.ONE, vpValue = 0, suit = Splendor.SuitIndex.GREEN, cost = [(Splendor.SuitIndex.BLUE,1),(Splendor.SuitIndex.BLACK,2)]))
    deck.level1Cards.append(Splendor.Card(level = Splendor.Level.ONE, vpValue = 0, suit = Splendor.SuitIndex.GREEN, cost = [(Splendor.SuitIndex.BLUE,1),(Splendor.SuitIndex.BLACK,2)]))
    deck.level1Cards.append(Splendor.Card(level = Splendor.Level.ONE, vpValue = 0, suit = Splendor.SuitIndex.GREEN, cost = [(Splendor.SuitIndex.BLUE,1),(Splendor.SuitIndex.BLACK,2)]))
    deck.level1Cards.append(Splendor.Card(level = Splendor.Level.ONE, vpValue = 0, suit = Splendor.SuitIndex.GREEN, cost = [(Splendor.SuitIndex.BLUE,1),(Splendor.SuitIndex.BLACK,2)]))
    deck.level1Cards.append(Splendor.Card(level = Splendor.Level.ONE, vpValue = 0, suit = Splendor.SuitIndex.GREEN, cost = [(Splendor.SuitIndex.BLUE,1),(Splendor.SuitIndex.BLACK,2)]))
    # 5: for convience, keep track of number of cards in each level
    deck.level1Cards.append(Splendor.Card(level = Splendor.Level.ONE, vpValue = 0, suit = Splendor.SuitIndex.GREEN, cost = [(Splendor.SuitIndex.BLUE,1),(Splendor.SuitIndex.BLACK,2)]))
    deck.level1Cards.append(Splendor.Card(level = Splendor.Level.ONE, vpValue = 0, suit = Splendor.SuitIndex.GREEN, cost = [(Splendor.SuitIndex.BLUE,1),(Splendor.SuitIndex.BLACK,2)]))
    deck.level1Cards.append(Splendor.Card(level = Splendor.Level.ONE, vpValue = 0, suit = Splendor.SuitIndex.GREEN, cost = [(Splendor.SuitIndex.BLUE,1),(Splendor.SuitIndex.BLACK,2)]))
    deck.level1Cards.append(Splendor.Card(level = Splendor.Level.ONE, vpValue = 0, suit = Splendor.SuitIndex.GREEN, cost = [(Splendor.SuitIndex.BLUE,1),(Splendor.SuitIndex.BLACK,2)]))
    deck.level1Cards.append(Splendor.Card(level = Splendor.Level.ONE, vpValue = 0, suit = Splendor.SuitIndex.GREEN, cost = [(Splendor.SuitIndex.BLUE,1),(Splendor.SuitIndex.BLACK,2)]))
    # 10
    deck.level1Cards.append(Splendor.Card(level = Splendor.Level.ONE, vpValue = 0, suit = Splendor.SuitIndex.GREEN, cost = [(Splendor.SuitIndex.BLUE,1),(Splendor.SuitIndex.BLACK,2)]))
    deck.level1Cards.append(Splendor.Card(level = Splendor.Level.ONE, vpValue = 0, suit = Splendor.SuitIndex.GREEN, cost = [(Splendor.SuitIndex.BLUE,1),(Splendor.SuitIndex.BLACK,2)]))
    deck.level1Cards.append(Splendor.Card(level = Splendor.Level.ONE, vpValue = 0, suit = Splendor.SuitIndex.GREEN, cost = [(Splendor.SuitIndex.BLUE,1),(Splendor.SuitIndex.BLACK,2)]))
    # 13

    # level 2
    deck.level2Cards.append(Splendor.Card(level = Splendor.Level.TWO, vpValue = 1, suit = Splendor.SuitIndex.WHITE, cost = [(Splendor.SuitIndex.GREEN,1),(Splendor.SuitIndex.BLUE,2),(Splendor.SuitIndex.RED,1),(Splendor.SuitIndex.WHITE,2)]))
    deck.level2Cards.append(Splendor.Card(level = Splendor.Level.TWO, vpValue = 1, suit = Splendor.SuitIndex.WHITE, cost = [(Splendor.SuitIndex.GREEN,1),(Splendor.SuitIndex.BLUE,2),(Splendor.SuitIndex.RED,1),(Splendor.SuitIndex.WHITE,2)]))
    deck.level2Cards.append(Splendor.Card(level = Splendor.Level.TWO, vpValue = 1, suit = Splendor.SuitIndex.WHITE, cost = [(Splendor.SuitIndex.GREEN,1),(Splendor.SuitIndex.BLUE,2),(Splendor.SuitIndex.RED,1),(Splendor.SuitIndex.WHITE,2)]))
    deck.level2Cards.append(Splendor.Card(level = Splendor.Level.TWO, vpValue = 1, suit = Splendor.SuitIndex.WHITE, cost = [(Splendor.SuitIndex.GREEN,1),(Splendor.SuitIndex.BLUE,2),(Splendor.SuitIndex.RED,1),(Splendor.SuitIndex.WHITE,2)]))
    deck.level2Cards.append(Splendor.Card(level = Splendor.Level.TWO, vpValue = 1, suit = Splendor.SuitIndex.WHITE, cost = [(Splendor.SuitIndex.GREEN,1),(Splendor.SuitIndex.BLUE,2),(Splendor.SuitIndex.RED,1),(Splendor.SuitIndex.WHITE,2)]))
    # 5
    deck.level2Cards.append(Splendor.Card(level = Splendor.Level.TWO, vpValue = 1, suit = Splendor.SuitIndex.WHITE, cost = [(Splendor.SuitIndex.GREEN,1),(Splendor.SuitIndex.BLUE,2),(Splendor.SuitIndex.RED,1),(Splendor.SuitIndex.WHITE,2)]))
    deck.level2Cards.append(Splendor.Card(level = Splendor.Level.TWO, vpValue = 1, suit = Splendor.SuitIndex.WHITE, cost = [(Splendor.SuitIndex.GREEN,1),(Splendor.SuitIndex.BLUE,2),(Splendor.SuitIndex.RED,1),(Splendor.SuitIndex.WHITE,2)]))
    deck.level2Cards.append(Splendor.Card(level = Splendor.Level.TWO, vpValue = 1, suit = Splendor.SuitIndex.WHITE, cost = [(Splendor.SuitIndex.GREEN,1),(Splendor.SuitIndex.BLUE,2),(Splendor.SuitIndex.RED,1),(Splendor.SuitIndex.WHITE,2)]))
    # 8
    
    # level 3
    deck.level3Cards.append(Splendor.Card(level = Splendor.Level.THREE, vpValue = 4, suit = Splendor.SuitIndex.BLACK, cost = [(Splendor.SuitIndex.GREEN,3),(Splendor.SuitIndex.BLUE,3),(Splendor.SuitIndex.RED,2),(Splendor.SuitIndex.WHITE,2),(Splendor.SuitIndex.BLACK,2)]))
    deck.level3Cards.append(Splendor.Card(level = Splendor.Level.THREE, vpValue = 4, suit = Splendor.SuitIndex.BLACK, cost = [(Splendor.SuitIndex.GREEN,3),(Splendor.SuitIndex.BLUE,3),(Splendor.SuitIndex.RED,2),(Splendor.SuitIndex.WHITE,2),(Splendor.SuitIndex.BLACK,2)]))
    deck.level3Cards.append(Splendor.Card(level = Splendor.Level.THREE, vpValue = 4, suit = Splendor.SuitIndex.BLACK, cost = [(Splendor.SuitIndex.GREEN,3),(Splendor.SuitIndex.BLUE,3),(Splendor.SuitIndex.RED,2),(Splendor.SuitIndex.WHITE,2),(Splendor.SuitIndex.BLACK,2)]))
    deck.level3Cards.append(Splendor.Card(level = Splendor.Level.THREE, vpValue = 4, suit = Splendor.SuitIndex.BLACK, cost = [(Splendor.SuitIndex.GREEN,3),(Splendor.SuitIndex.BLUE,3),(Splendor.SuitIndex.RED,2),(Splendor.SuitIndex.WHITE,2),(Splendor.SuitIndex.BLACK,2)]))
    deck.level3Cards.append(Splendor.Card(level = Splendor.Level.THREE, vpValue = 4, suit = Splendor.SuitIndex.BLACK, cost = [(Splendor.SuitIndex.GREEN,3),(Splendor.SuitIndex.BLUE,3),(Splendor.SuitIndex.RED,2),(Splendor.SuitIndex.WHITE,2),(Splendor.SuitIndex.BLACK,2)]))
    # 5
    deck.level3Cards.append(Splendor.Card(level = Splendor.Level.THREE, vpValue = 4, suit = Splendor.SuitIndex.BLACK, cost = [(Splendor.SuitIndex.GREEN,3),(Splendor.SuitIndex.BLUE,3),(Splendor.SuitIndex.RED,2),(Splendor.SuitIndex.WHITE,2),(Splendor.SuitIndex.BLACK,2)]))
    # 6

    return deck
