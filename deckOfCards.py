import random
#Author - Dan Rabinowitz
#Create a card class
class card:

    #Set the suit and rank of the card
    def __init__ (self, rank, suit):
        self.__rank = rank
        self.__suit = suit

    #Get the rank of a card
    def getRank(self):
        return self.__rank

    #Get the suit of a card
    def getSuit(self):
        return self.__suit

    #Get the blackjack value of the card
    def BJValue(self):
        if self.__rank < 11:
            return self.__rank
        else:
            return 10

    #Name the card
    def __str__(self):
        if self.__suit =="d":
            suitName = "Diamonds"
        elif self.__suit =="h":
            suitName = "Hearts"
        elif self.__suit =="s":
            suitName = "Spades"
        elif self.__suit =="c":
            suitName = "Clubs"
        ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack",  "Queen", "King"]
        realRank = ranks[int(self.__rank) - 1]
        card = realRank + " of " + suitName
        return card
        
#Create a deck of cards
class Deck:

    #Create the 52 card deck
    def __init__(self):
        self.__numCards = 0
        self.__cards = []
        suitNames = ["d","h","s","c"]
        for suit in range(4):
            for rank in range(1, 14):
                self.__cards.append(card(rank, suitNames[suit]))
                self.__numCards +=1

    #Draw the top card
    def drawTop(self):
        self.__numCards -= 1
        return self.__cards.pop(0)
        

    #Draw a random card
    def drawRandom(self):
        self.__numCards -= 1
        return self.__cards.pop(random.randint(0,self.__numCards-1))

    #Return a card to the bottom of the deck
    def returnCardtoDeck(self, card):
        self.__numCards += 1
        self.__cards.append(card)

    #Get the number of cards in the deck
    def getNumCards(self):
        return self.__numCards
    
