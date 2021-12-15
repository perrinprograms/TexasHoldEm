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
    
    def createDeck(self):
        print("this function is getting called")
        suits = [Suit("Hearts"),Suit("Diamonds"),Suit("Clubs"),Suit("Spades")]
        cardValues = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

        for value in cardValues:
            for suit in suits:
                self.cards.append(Card(suit.name,value))

deck = Deck()
deck.createDeck()

for card in deck.cards:
    print (f'{card.value} of {card.suit} ' )
    


        




