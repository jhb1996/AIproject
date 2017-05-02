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
		Player.money = 25000

class AI:
	money = 0
	def __init__(self):
		Player.money = 25000

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

#########################################################
"""all endgame checking functions return 1 or 0 followed
	by best 5 cards numbers in order. eg 1, [3, 3, 3, K, T]
	returns 0, [0,0,0,0,0] if false. Only guarenteed to work
	when there is no better hand eg full house may return 0
	if 4 of a kind are present"""

def checkStraightFlush(hole_cards, shared_cards):
	available=hole_cards+shared_cards
	availableSuits=[]
	availableVals=[]
	suitedVals=[-1]*len(available)
	for x in range(len(available)):
		current=available[x]
		availableSuits.append(current.suit)
		availableVals.append(current.num_value())
	
	FlushSuit='0'
	Flush=False
	if availableSuits.count('H') >= 5:
		FlushSuit='H'
		Flush=True
	elif availableSuits.count('S') >= 5:
		FlushSuit='S'
		Flush=True
	elif availableSuits.count('C') >= 5:
		Flush=True
		FlushSuit='C'
	elif availableSuits.count('D') >= 5:
		Flush=True
		FlushSuit='D'
	
	if Flush==True:	
		for x in range(len(availableSuits)):
			currentVal=availableVals[x]
			if availableSuits[x]==FlushSuit and (currentVal not in suitedVals):
				suitedVals[x]=currentVal
				#print(suitedVals[x])
				if currentVal== 14:
					suitedVals.append(1)
				#print(suitedVals)
		
		
		
	suitedVals.sort(reverse=True)
	for x in range(len(suitedVals)-4):

		if suitedVals[x] == suitedVals[x+1]+1 and suitedVals[x] == suitedVals[x+2]+2 and suitedVals[x] == suitedVals[x+3]+3 and suitedVals[x] == suitedVals[x+4]+4: 
			return True,[suitedVals[x], suitedVals[x+1], suitedVals[x+2], suitedVals[x+3], suitedVals[x+4]]
	return False, [0, 0 ,0, 0, 0] 

def checkStraight(hole_cards, shared_cards):

	available=hole_cards+shared_cards

	for x in range (len(available)):
		if available[x].num_value() not in available:
			available[x]=available[x].num_value()
			if available[x] == 14:
				available.append(1)
		else:
			available[x]=-1
	available.sort(reverse=True)
	for x in range(len(available)-4):

			if available[x] == available[x+1]+1 and available[x] == available[x+2]+2 and available[x] == available[x+3]+3 and available[x] == available[x+4]+4: 
				return True,[available[x], available[x+1], available[x+2], available[x+3], available[x+4]]
	return False, [0, 0, 0, 0, 0]


def checkFlush(hole_cards, shared_cards):
	available=hole_cards+shared_cards
	availableSuits=[]
	availableVals=[]

	for x in range(len(available)):
		availableSuits.append(available[x].suit)
		availableVals.append(available[x].num_value())
	if availableSuits.count('H') >= 5 or availableSuits.count('C') >= 5 or availableSuits.count('D') >= 5 or availableSuits.count('S') >= 5:
		print("test")
		#print(availableVals)
		availableVals.sort(reverse=True)
		
		return True, availableVals[:5]
	return False, [0, 0 ,0, 0, 0] 


def checkFourOfAKind(hole_cards, shared_cards):
	available=hole_cards+shared_cards

	for x in range(len(available)):
		available[x]= available[x].num_value()
	for num in range(14, 1, -1): 
		if available.count(num) == 4: 
			for n in range (14, 2, -1): 
				if available.count(n) >= 1 and available.count(n) < 4: 
					return True, [num, num, num,num, n]
	return False, [0, 0, 0, 0, 0]

def checkFullHouse(hole_cards, shared_cards):
	available=hole_cards+shared_cards
	for x in range(len(available)):
		available[x]= available[x].num_value()
	for num in range(14, 1, -1):
		if available.count(num) == 3:
			for num2 in range(14, 1, -1): 
				if available.count(num2) >= 2 and num2!=num : 
					return True, [num, num, num, num2, num2] 
	return False, [0, 0 ,0, 0, 0] 

def checkThreeOfAKind(hole_cards, shared_cards):
	available=hole_cards+shared_cards

	for x in range (len(available)):
		available[x]= available[x].num_value()
	for num in range(14, 1, -1): 
		#print(available.count(num) == 2)
		if available.count(num) == 3: 
			for n in range (14, 2, -1): 
				#print(n)
				if available.count(n) == 1: 
					for m in range(n-1, 2, -1): 
						if available.count(m) == 1:
							return True,[num, num, num, n, m]
	return False, [0, 0, 0, 0, 0]

def checkTwoPair(hole_cards, shared_cards):
	available=hole_cards+shared_cards
	for x in range(len(available)):
		available[x]= available[x].num_value()
	for num in range(14, 1, -1): 
		if available.count(num) == 2: 
			for num2 in range(num-1, 1, -1): 
				if available.count(num2) == 2: 
					for n in range (14, 2, -1): 
						if available.count(n) == 1: 
							return True, [num, num, num2, num2, n] 
	return False, [0, 0 ,0, 0, 0] 

def checkOnePair(hole_cards, shared_cards):
	available=hole_cards+shared_cards
	for x in range(len(available)):
		available[x]= available[x].num_value()
		#print (available[x])
		#print("test")
	for num in range(14, 1, -1): 
		#print(available.count(num) == 2)
		if available.count(num) == 2: 
			for n in range (14, 2, -1): 
				print(n)
				if available.count(n) == 1: 
					for m in range(n-1, 2, -1): 
						if available.count(m) == 1: 
							for o in range (m-1, 2, -1): 
								if available.count(o) == 1:
									return True, [num, num, n, m, o] 
	return False, [0,0,0, 0, 0] 

def checkHighCard(hole_cards, shared_cards):
	available=hole_cards+shared_cards
	for x in range(len(available)):
		available[x]= available[x].num_value()
	available.sort(reverse=True)
	return True, [available[:5]]
	
if __name__ == '__main__':
	card1=Card("K",'C')
	card2=Card("Q",'C')
	card3=Card("2",'H')
	card4=Card("9",'C')
	card5=Card("3",'C')
	card6=Card("5", 'C')
	card7=Card("6",'C')
	hole_cards=[card1, card2]
	shared_cards=[card3, card4, card5, card6, card7,]
	truth, best_five = checkHighCard(hole_cards, shared_cards)
	
	print(truth, best_five)

    