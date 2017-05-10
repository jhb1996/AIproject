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
	suitedVals=[-1]*len(available)
	
	for x in range(len(available)):
		availableSuits.append(available[x].suit)
		availableVals.append(available[x].num_value())
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
		FlushSuit='D'		#print(availableVals)
		
	if Flush==True:	
		for x in range(len(availableSuits)):
			currentVal=availableVals[x]
			if availableSuits[x]==FlushSuit and (currentVal not in suitedVals):
				print currentVal
				suitedVals[x]=currentVal
		suitedVals.sort(reverse=True)
		
		return True, suitedVals[:5]
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
			for n in range (14, 1, -1): 
				if available.count(n) == 1: 
					for m in range(n-1, 1, -1):
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
	for num in range(14, 1, -1): 
		if available.count(num) == 2: 
			for n in range (14, 2, -1): 
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
	return True, available[:5]
	
"""takes the AIcards (a list of two card objects), the Oponent
	cards and the table cards (a list of 5 card objects)
	and returns a winner. Returns 1 if AI wins, -1 if player wins
	and 0 if tie"""
def findWinner(AI_cards, Player_cards, shared_cards):
	
	AItruth, AIbest_five = checkStraightFlush(AI_cards, shared_cards)
	Playertruth, Playerbest_five = checkStraightFlush(Player_cards, shared_cards)
	if AItruth==True and Playertruth==False:
		return 1
	elif AItruth==False and Playertruth==True:
		return -1
	elif AItruth==True and Playertruth==True:
		if AIbest_five[0]>Playerbest_five[0]:
			return 1
		elif Playerbest_five[0]<AIbest_five[0]:
			return -1
		else: return 0
	
	AItruth, AIbest_five = checkFourOfAKind(AI_cards, shared_cards)
	Playertruth, Playerbest_five = checkFourOfAKind(Player_cards, shared_cards)
	if AItruth==True and Playertruth==False:
		return 1
	elif AItruth==False and Playertruth==True:
		return -1
	elif AItruth==True and Playertruth==True:
		if AIbest_five[0]>Playerbest_five[0] or (AIbest_five[0]==Playerbest_five[0] and AIbest_five[4]>Playerbest_five[4]):
			return 1
		elif AIbest_five[0]<Playerbest_five[0] or (AIbest_five[0]==Playerbest_five[0] and AIbest_five[4]<Playerbest_five[4]):
			return -1
		else: return 0
	
	AItruth, AIbest_five = checkFullHouse(AI_cards, shared_cards)
	Playertruth, Playerbest_five = checkFullHouse(Player_cards, shared_cards)
	if AItruth==True and Playertruth==False:
		return 1
	elif AItruth==False and Playertruth==True:
		return -1
	elif AItruth==True and Playertruth==True:
		if AIbest_five[0]>Playerbest_five[0] or (AIbest_five[0]==Playerbest_five[0] and AIbest_five[3]>Playerbest_five[3]):
			return 1
		elif AIbest_five[0]<Playerbest_five[0] or (AIbest_five[0]==Playerbest_five[0] and AIbest_five[3]<Playerbest_five[3]):
			return -1
		else: return 0
		
	AItruth, AIbest_five = checkFlush(AI_cards, shared_cards)
	Playertruth, Playerbest_five = checkFlush(Player_cards, shared_cards)
	if AItruth==True and Playertruth==False:
		return 1
	elif AItruth==False and Playertruth==True:
		return -1
	elif AItruth==True and Playertruth==True:
		if AIbest_five[0]>Playerbest_five[0]:return 1
		elif AIbest_five[0]<Playerbest_five[0]:return-1
		elif AIbest_five[1]>Playerbest_five[1]:return 1
		elif AIbest_five[1]<Playerbest_five[1]:return-1
		elif AIbest_five[2]>Playerbest_five[2]:return 1
		elif AIbest_five[2]<Playerbest_five[2]:return-1
		elif AIbest_five[3]>Playerbest_five[3]:return 1
		elif AIbest_five[3]<Playerbest_five[3]:return-1
		elif AIbest_five[4]>Playerbest_five[4]:return 1
		elif AIbest_five[4]<Playerbest_five[4]:return-1
		else: return 0
	
	AItruth, AIbest_five = checkStraight(AI_cards, shared_cards)
	Playertruth, Playerbest_five = checkStraight(Player_cards, shared_cards)
	if AItruth==True and Playertruth==False:
		return 1
	elif AItruth==False and Playertruth==True:
		return -1
	elif AItruth==True and Playertruth==True:
		if AIbest_five[0]>Playerbest_five[0] or (AIbest_five[0]==Playerbest_five[0] and AIbest_five[3]>Playerbest_five[3]):
			return 1
		elif AIbest_five[0]<Playerbest_five[0]:
			return -1
		else: return 0
	
	AItruth, AIbest_five = checkThreeOfAKind(AI_cards, shared_cards)
	Playertruth, Playerbest_five = checkThreeOfAKind(Player_cards, shared_cards)
	if AItruth==True and Playertruth==False:
		return 1
	elif AItruth==False and Playertruth==True:
		return -1
	elif AItruth==True and Playertruth==True:
		if AIbest_five[0]>Playerbest_five[0]:return 1
		elif AIbest_five[0]<Playerbest_five[0]:return -1
		elif AIbest_five[3]>Playerbest_five[3]:return 1
		elif AIbest_five[3]<Playerbest_five[3]:return -1
		elif AIbest_five[4]>Playerbest_five[4]:return 1
		elif AIbest_five[4]<Playerbest_five[4]:return -1
		else: return 0
	
	AItruth, AIbest_five = checkTwoPair(AI_cards, shared_cards)
	Playertruth, Playerbest_five = checkTwoPair(Player_cards, shared_cards)
	if AItruth==True and Playertruth==False:
		return 1
	elif AItruth==False and Playertruth==True:
		return -1
	elif AItruth==True and Playertruth==True:
		if AIbest_five[0]>Playerbest_five[0]:return 1
		elif AIbest_five[0]<Playerbest_five[0]:return -1
		elif AIbest_five[2]>Playerbest_five[2]:return 1
		elif AIbest_five[2]<Playerbest_five[2]:return -1
		elif AIbest_five[4]>Playerbest_five[4]:return 1
		elif AIbest_five[4]<Playerbest_five[4]:return -1
		else: return 0
		
	AItruth, AIbest_five = checkOnePair(AI_cards, shared_cards)
	Playertruth, Playerbest_five = checkOnePair(Player_cards, shared_cards)
	if AItruth==True and Playertruth==False:
		return 1
	elif AItruth==False and Playertruth==True:
		return -1
	elif AItruth==True and Playertruth==True:
		if AIbest_five[0]>Playerbest_five[0]:return 1
		elif AIbest_five[0]<Playerbest_five[0]:return -1
		elif AIbest_five[2]>Playerbest_five[2]:return 1
		elif AIbest_five[2]<Playerbest_five[2]:return -1
		elif AIbest_five[3]>Playerbest_five[3]:return 1
		elif AIbest_five[3]<Playerbest_five[3]:return -1
		elif AIbest_five[4]>Playerbest_five[4]:return 1
		elif AIbest_five[4]<Playerbest_five[4]:return -1
		else: return 0
		
	AItruth, AIbest_five = checkHighCard(AI_cards, shared_cards)
	Playertruth, Playerbest_five = checkHighCard(Player_cards, shared_cards)
	if AItruth==True and Playertruth==False:
		return 1
	elif AItruth==False and Playertruth==True:
		return -1
	elif AItruth==True and Playertruth==True:
		if AIbest_five[0]>Playerbest_five[0]:return 1
		elif AIbest_five[0]<Playerbest_five[0]:return -1
		elif AIbest_five[2]>Playerbest_five[2]:return 1
		elif AIbest_five[2]<Playerbest_five[2]:return -1
		elif AIbest_five[3]>Playerbest_five[3]:return 1
		elif AIbest_five[3]<Playerbest_five[3]:return -1
		elif AIbest_five[4]>Playerbest_five[4]:return 1
		elif AIbest_five[4]<Playerbest_five[4]:return -1
		else: return 0
	#truth, best_five = checkFourofAKind(hole_cards, shared_cards)
	#truth, best_five = checkFullHouse(hole_cards, shared_cards)
	#truth, best_five = checkFlush(hole_cards, shared_cards)
	#truth, best_five = checkStraight(hole_cards, shared_cards)
	#truth, best_five = checkThreeOfAKind(hole_cards, shared_cards)
	#truth, best_five = checkTwoPair(hole_cards, shared_cards)
	#truth, best_five = checkOnePair(hole_cards, shared_cards)
	#truth, best_five = checkHighCard(hole_cards, shared_cards)

def checkFlushDraw(hole_cards, shared_cards):
	available=hole_cards+shared_cards
	availableSuits=[]
	availableVals=[]
	suitedVals=[-1]*len(available)
	
	for x in range(len(available)):
		availableSuits.append(available[x].suit)
		availableVals.append(available[x].num_value())
	FlushSuit='0'
	Flush=False
	if availableSuits.count('H') == 4:
		FlushSuit='H'
		Flush=True
	elif availableSuits.count('S') == 4:
		FlushSuit='S'
		Flush=True
	elif availableSuits.count('C') == 4:
		Flush=True
		FlushSuit='C'
	elif availableSuits.count('D') == 4:
		Flush=True
		FlushSuit='D'
		
	if Flush==True:	
		for x in range(len(availableSuits)):
			currentVal=availableVals[x]
			if availableSuits[x]==FlushSuit and (currentVal not in suitedVals):
				suitedVals[x]=currentVal
		suitedVals.sort(reverse=True)
		
		return True, suitedVals[:4]
	return False, [0, 0 ,0, 0]

def checkGutShot(hole_cards, shared_cards):

	available=hole_cards+shared_cards

	for x in range (len(available)):
		if available[x].num_value() not in available:
			available[x]=available[x].num_value()
			if available[x] == 14:
				available.append(1)
		else:
			available[x]=-1
	available.sort(reverse=True)
	for x in range(len(available)-3):
			if available[x] == available[x+1]+2 and available[x]== available[x+2]+3 and available[x] == available[x+3]+4: 
				return True, available[x:x+4]#, available[x+1], available[x+2], available[x+3] ]
			if available[x] == available[x+1]+1 and available[x]== available[x+2]+3 and available[x] == available[x+3]+4: 
				return True, available[x:x+4]#], available[x+1], available[x+2], available[x+3] ]
			if available[x] == available[x+1]+1 and available[x]== available[x+2]+2 and available[x] == available[x+3]+4: 
				return True, available[x:x+4]
			
	return False, [0, 0, 0, 0]

def checkOpenEnder(hole_cards, shared_cards):

	available=hole_cards+shared_cards

	for x in range (len(available)):
		if available[x].num_value() not in available:
			available[x]=available[x].num_value()
			if available[x] == 14:
				available.append(1)
		else:
			available[x]=-1
	available.sort(reverse=True)
	for x in range(len(available)-3):
			if (available[x] == available[x+1]+1 and available[x]== available[x+2]+2 and available[x] == available[x+3]+3) and available[x+3]!=1 and available[x]!=14: 
				return True, available[x:x+4]

			
	return False, [0, 0, 0, 0]

def checkBackdoorFlush(hole_cards, shared_cards):
	available=hole_cards+shared_cards
	availableSuits=[]
	availableVals=[]
	suitedVals=[-1]*len(available)
	
	for x in range(len(available)):
		availableSuits.append(available[x].suit)
		availableVals.append(available[x].num_value())
	FlushSuit='0'
	Flush=False
	if availableSuits.count('H') == 3:
		FlushSuit='H'
		Flush=True
	elif availableSuits.count('S') == 3:
		FlushSuit='S'
		Flush=True
	elif availableSuits.count('C') == 3:
		Flush=True
		FlushSuit='C'
	elif availableSuits.count('D') == 3:
		Flush=True
		FlushSuit='D'
		
	if Flush==True:	
		for x in range(len(availableSuits)):
			currentVal=availableVals[x]
			if availableSuits[x]==FlushSuit and (currentVal not in suitedVals):
				suitedVals[x]=currentVal
		suitedVals.sort(reverse=True)
		
		return True, suitedVals[:3]
	return False, [0, 0 ,0]

def checkBackdoorStraight(hole_cards, shared_cards):

	available=hole_cards+shared_cards

	for x in range (len(available)):
		if available[x].num_value() not in available:
			available[x]=available[x].num_value()
			if available[x] == 14:
				available.append(1)
		else:
			available[x]=-1
	available.sort(reverse=True)
	for x in range(len(available)-2):
			if available[x] == available[x+1]+1 and available[x]== available[x+2]+2:
				return True, available[x:x+3]
			if available[x] == available[x+1]+1 and available[x]== available[x+2]+3: 
				return True, available[x:x+3]
			if available[x] == available[x+1]+1 and available[x]== available[x+2]+4:
				return True, available[x:x+3]
			if available[x] == available[x+1]+1 and available[x]== available[x+2]+3: 
				return True, available[x:x+3]
			if available[x] == available[x+1]+2 and available[x]== available[x+2]+3:
				return True, available[x:x+3]
			if available[x] == available[x+1]+2 and available[x]== available[x+2]+4: 
				return True, available[x:x+3]
			if available[x] == available[x+1]+3 and available[x]== available[x+2]+4:
				return True, available[x:x+3]

	return False, [0, 0, 0]

def checkSetThree(hole_cards, shared_cards):
	length=len(shared_cards)
	shared_vals=[-1]*length

	for x in range (length):
		shared_vals[x] = shared_cards[x].num_value()
	if hole_cards[0].num_value()==hole_cards[1].num_value():
		num = hole_cards[0].num_value()
		if num in shared_vals: return True, [num, num, num]
		
	return False, [0, 0, 0]

def checkTripThree(hole_cards, shared_cards):
	length=len(shared_cards)
	shared_vals=[-1]*length
	
	for x in range (length):
		shared_vals[x] = shared_cards[x].num_value()
	val1=hole_cards[0].num_value()
	if shared_vals.count(val1)==2:
		return True, [val1, val1, val1]
	val2=hole_cards[1].num_value()
	if shared_vals.count(val1)==2:
		return True, [val1, val1, val1]
	return False, [0, 0, 0]

def checkHighKicker(hole_cards, shared_cards):
	length=len(shared_cards)
	shared_vals=[-1]*length
	
	val1=hole_cards[0].num_value()
	val2=hole_cards[1].num_value()

	if (val1 == 14 or val2==14):
		return True, [14]
	if (val1 == 13 or val2==13):
		return True, [13]
	return False, [0]

def checkGoodKicker(hole_cards, shared_cards):
	length=len(shared_cards)
	shared_vals=[-1]*length
	
	val1=hole_cards[0].num_value()
	val2=hole_cards[1].num_value()

	if (val1 == 12 or val2==12):
		return True, [12]
	if (val1 == 11 or val2==11):
		return True, [11]
	if (val1 == 10 or val2==10):
		return True, [10]
	return False, [0]

def checkOverPair(hole_cards, shared_cards):
	val1=hole_cards[0].num_value()
	val2=hole_cards[1].num_value()

	if (val1 == val2):
			length=len(shared_cards)		
			shared_vals=[-1]*length
			y=0
			for x in range (length):
				y=y+( val1>shared_cards[x].num_value())
			if y ==x+1: return True, [0]
	return False, [0]


def checkUnderPair(hole_cards, shared_cards):
	val1=hole_cards[0].num_value()
	val2=hole_cards[1].num_value()

	if (val1 == val2):
			length=len(shared_cards)		
			shared_vals=[-1]*length
			y=0
			for x in range (length):
				y=y+(val1<shared_cards[x].num_value())
			if y ==x+1: return True, [0]
	return False, [0]

def checkHighPair(hole_cards, shared_cards):
	val1=hole_cards[0].num_value()
	val2=hole_cards[1].num_value()
	length=len(shared_cards)		
	shared_vals=[-1]*length
	for x in range (length):
		shared_vals[x]=shared_cards[x].num_value()
	shared_vals.sort(reverse=True)
	biggest = shared_vals[0]
	if val1==biggest or val2==biggest:
		return True, [val1,val1]
	return False, [0]

def checkLowPair(hole_cards, shared_cards):
	val1=hole_cards[0].num_value()
	val2=hole_cards[1].num_value()
	length=len(shared_cards)		
	shared_vals=[-1]*length
	for x in range (length):
		shared_vals[x]=shared_cards[x].num_value()
	shared_vals.sort(reverse=False)
	smallest = shared_vals[0]
	if val1==smallest or val2==smallest:
		return True, [val1,val1]
	return False, [0]

def checkMiddlePair(hole_cards, shared_cards):
	val1=hole_cards[0].num_value()
	val2=hole_cards[1].num_value()
	length=len(shared_cards)		
	shared_vals=[-1]*length
	for x in range (length):
		shared_vals[x]=shared_cards[x].num_value()
	shared_vals.sort(reverse=True)
	middle = shared_vals[1:length-1]
	if val1 in middle or val2==middle:
		return True, [val1,val1]
	return False, [0]

if __name__ == '__main__':
	AI_card1=Card("K",'C')
	AI_card2=Card("J",'H')
	
	Player_card1=Card("3",'D')
	Player_card2=Card("J",'H')
	
	card3=Card("K", 'C')
	card4=Card("3", 'H')
	card5=Card("4", 'S')
	#card6=Card("4", 'C')
	#card7=Card("5", 'S')
	
	AI_cards=[AI_card1, AI_card2]
	Player_cards=[Player_card1, Player_card2]
	shared_cards=[card3, card4, card5]#, card6, card7,]
	truth, best_five = checkMiddlePair(AI_cards, shared_cards)
	print(truth, best_five)
	winner=findWinner(AI_cards, Player_cards, shared_cards)	
	print(winner)



