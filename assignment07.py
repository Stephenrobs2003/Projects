import random

# Function to generate a deck of 52 cards represented by integers 0 to 51
def generateDeck():
   myList = []
   for i in range(52):
      myList = myList + [i]
   return myList

# Function to get the rank of a card (2 to 14, where 11=Jack, 12=Queen, 13=King, 14=Ace)
def getCardRank(c):
   value = (c // 4) + 2
   return value

# Function to get the suit of a card (clubs, diamonds, hearts, spades)
def getCardSuit(c):
   if c == 0:
      return "clubs"
   if c == 1:
      return "diamonds"
   if c == 2:
      return "hearts"
   if c == 3:
      return "spades"
   else:
      for i in range(3, 52):
         if c % 4 == 0:
            return "clubs"
         if c % 4 == 1:
            return "diamonds"
         if c % 4 == 2:
            return "hearts"
         if c % 4 == 3:
            return "spades"

# Function to get the display string of a card (e.g., "2 of clubs", "jack of hearts")
def getCardDisplay(c):
   value = (c // 4) + 2
   suit = getCardSuit(c)
   if value <= 10:
      return f'{value} of {suit}'
   if value == 11:
      return f'jack of {suit}'
   if value == 12:
      return f'queen of {suit}'
   if value == 13:
      return f'king of {suit}'
   if value == 14:
      return f'ace of {suit}'

# Function to display all cards in the deck (currently not implemented)
def displayAllCards(cards):
   integers = []
   cards = generateDeck()

# Function to deal 'n' cards to each hand from the deck
def dealCards(hands, cards, n):
   if n * len(hands) > len(cards):
      print("error")
      return
   for i in range(n):
      for h in range(len(hands)):
         c = cards.pop(0)
         hands[h].append(c)
   return hands
