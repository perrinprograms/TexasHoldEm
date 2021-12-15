import random


class Suit:
    def __init__(self,name):
        self.name = name
    
class Card(): 
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value


class Deck():
    def __init__(self):
        self.cards = []

    def __index__(self):
        return self

    def createDeck(self):

        suits = [Suit("Hearts"),Suit("Diamonds"),Suit("Clubs"),Suit("Spades")]
        cardValues = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

        for value in cardValues:
            for suit in suits:
                self.cards.append(Card(suit.name,value))

    def shuffleDeck(self):
        shuffledOrder = []
        shuffledDeck = []

        #outer loop that stops when the new random card order has reached the same length as the deck count
        while len(shuffledOrder) != len(self.cards):
            #getting a random number between 0 and the length of the amount of the deck count. 
            randIndex = random.randint(0,len(self.cards) -1)
            
            #making sure there are no duplicates in the list
            if randIndex not in shuffledOrder:
                #adding the random index to a list
                shuffledOrder.append(randIndex)
        
        for randIndex in shuffledOrder:
            #looping through the randomly ordered list of numbers and adding a card in a random order to a new list
            shuffledDeck.append(self.cards[randIndex])

        #reassigning the ordered deck to the shuffled deck
        self.cards = shuffledDeck