import random

def generateDeck():
   myList = []
   for i in range(52):
      myList = myList + [i]
   return myList

def getCardRank(c):
   value = (c//4)+2
   return value

def getCardSuit(c):
   if c == 0:
      return "clubs"
   if c== 1:
      return "diamonds"
   if c == 2:
      return "hearts"
   if c == 3:
      return "spades"
   else:
      for i in range(3,52):
         if  c % 4 == 0:
            return "clubs"
         if c % 4 == 1:
            return "diamonds"
         if c % 4 == 2:
            return "hearts"
         if c % 4 == 3:
            return "spades"

def getCardDisplay(c):
   value = (c//4) + 2
   suit = getCardSuit(c)
   if value <= 10:
      return (f'{value} of {suit}')
   if value == 11:
      return (f'jack of {suit}')
   if value == 12:
      return (f'queen of {suit}')
   if value == 13:
      return (f'king of {suit}')
   if value == 14:
      return (f'ace of {suit}')

def displayAllCards(cards):
   integers = []
   cards = generateDeck()

def dealCards(hands,cards,n):
   if n * len(hands) > len(cards):
      print("error")
      return
   for i in range(n):
      for h in range(len(hands)):
         c= cards.pop(0)
         hands[h].append(c)
   return hands




