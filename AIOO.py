import random
import collections

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def card(self):
		print self.value + self.suit

	def value(self):
		return self.value
	def suit(self):
		return self.suit
	def num_value(self):
		if self.value is 'A':
			return 14
		elif self.value is 'K':
			return 13
		elif self.value is 'Q':
			return 12
		elif self.value is 'J':
			return 11
		elif self.value is 'T':
			return 10
		else:
			return int (self.value) 
class Deck:
	extra_suits = ['T','J','Q','K','A']
	def __init__(self):
		self.cards = []
		for i in range(2,10):
			self.cards.append(Card(str(i),'C'))
			self.cards.append(Card(str(i),'D'))
			self.cards.append(Card(str(i),'H'))
			self.cards.append(Card(str(i),'S'))
		for i in range (0, len(Deck.extra_suits)):
			self.cards.append(Card(Deck.extra_suits[i],'C'))
			self.cards.append(Card(Deck.extra_suits[i],'D'))
			self.cards.append(Card(Deck.extra_suits[i],'H'))
			self.cards.append(Card(Deck.extra_suits[i],'S'))
		random.shuffle(self.cards)

	def deck(self):
		for i in range (0,len(self.cards)):
			self.cards[i].card()

	def dealCard(self):
		return self.cards.pop(0)


class Hand:
	hole_cards = []
	shared_cards = []

	def __init__(self,card1,card2):
		Hand.hole_cards.append(card1)
		Hand.hole_cards.append(card2)


class Player:
	money = 0
	def __init__(self):
		Player.money = 2500

class AI:
	money = 0
	def __init__(self):
		Player.money = 2500

def preflopHand(card1,card2):
	suited = 'o'
	if card1.suit is card2.suit:
		suited = 's'
	if (card1.num_value > card2.num_value):
		return card1.value + card2.value + suited
	else:
		return card2.value + card1.value + suited
def preflopHandRank(hand):
	f = open("Preflop_strength_chart.txt",'r')
	for i in range(0,169):
		line = f.readline()
		if hand in line:
			return line.split('	')[0]
	return 2000






#tests to be deleted
d = Deck()
d.deck()
print('')
print('')
card1 = d.dealCard()
card2 = d.dealCard()
print('')
print('')
d.deck()
print('')
print('')
print preflopHand(card1,card2)
print preflopHandRank(preflopHand(card1,card2))


#c = Card('2','H')
#c.card()
#d = Deck()
#d.deck()
