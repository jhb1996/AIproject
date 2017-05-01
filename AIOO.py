import random
import collections

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def card(self):
		return self.value + self.suit

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
			print self.cards[i].card()

	def dealCard(self):
		return self.cards.pop(0)


class Hand:
	hole_cards = []
	shared_cards = []

	def __init__(self,card1,card2):
		Hand.hole_cards.append(card1)
		Hand.hole_cards.append(card2)


class Player:
	def __init__(self):
		self.money = 25000

	def get_money(self):
		return self.money

	def set_money(self,amount):
		self.money = amount

class AI:
	def __init__(self):
		self.money = 25000

	def get_money(self):
		return self.money

	def set_money(self,amount):
		self.money = amount

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

def postFlopHandValue(hole_cards,table_cards):

	straightFlush = False
	quads = False
	fullHouse = False
	flush = False #done
	straight = False
	set3 = False
	ThreeOfAKind = False
	twoPair = False
	overPair = False
	highPair = False
	flushDraw = False
	openEnder = False
	gutShot = False
	mediumPair = False
	lowPair = False
	underPair = False
	highKicker = False
	goodKicker = False
	backdoorFlush = False
	backdoorStraight = False

	#todo determine all of this

def postFlopBoardScare(table_cards):
	
	table_card_values = []
	for x in table_cards:
		table_card_values.append(x.num_value)

	table_card_values.sort()

	flush3 = False
	flush2 = False
	straight3 = False
	straight4 = False
	straight5 = False
	triple = False
	double = False

	if table_cards[0].suit() is table_cards[1].suit() is table_cards[2].suit():
		flush3 = True
	elif table_cards[0].suit() is table_cards[1].suit() or table_cards[1].suit() is table_cards[2].suit() or table_cards[0].suit() is table_cards[2].suit():
		flush2 = True

	if table_cards[0].value() is table_cards[1].value() is table_cards[2].value():
		triple = True
	elif table_cards[0].value() is table_cards[1].value() or table_cards[1].value() is table_cards[2].value() or table_cards[0].value() is table_cards[2].value():
		double = True
	elif (table_card_values[2] - table_card_values[0]) is 2:
		straight3 = True
	elif (table_card_values[2] - table_card_values[0]) is 3:
		straight4 = True
	elif (table_card_values[2] - table_card_values[0]) is 4:
		straight5 = True

	if straight3 and flush3:
		return 5
	elif (double and flush2) or flush3:
		return 4
	elif triple or straight4 or straight3 or double:
		return 3
	elif flush2 or straight5:
		return 2
	else:
		return 1 

def play_preflop(plm, aim, first, player_cards, ai_cards):
	player_money = plm
	ai_money = aim
	pot = 0
	player_call = False
	ai_call = False
	current_bet = False
	if first:
		print ('\n you bet first. To check just bet $0 ')

	while not player_call or not ai_call:
		if first:
			while True:
				print ("The current_bet it : $" + str(current_bet))
				print ("Please type how much you want to bet or type 'fold' ")
				var = raw_input('')
				if var is 'fold':
					player_call =True
					ai_call = True
					#ai wins stuff
					break
				elif int(var) is current_bet:
					first = False
					player_call = True
					player_money = player_money- int(var)
					pot = pot + int(var)
					break
				elif int(var) < current_bet:
					print('You did not match the current bet. You must bet at least that to call or more to raise')
				else:
					first = False
					player_call = True
					ai_call = False
					current_bet = int(var) - current_bet()
					#need to finish 



		else:
			a = 1



def play_hand(player, ai, first):
	player_money = player.get_money()
	ai_money = ai.get_money()
	print ("You currently have : $" + str(player_money))
	print ("Your apponent has: $" +str(ai_money))
	deck = Deck()
	player_cards = []
	ai_cards = []
	card1 = deck.dealCard()
	card2 = deck.dealCard()
	card3 = deck.dealCard()
	card4 = deck.dealCard()
	player_cards.append(card1)
	player_cards.append(card3)
	ai_cards.append(card2)
	ai_cards.append(card4)
	print('\nYou have been delt: ' + card1.card() + ' ' + card3.card())


	


def play_game():
	player = Player()
	ai = AI ()
	print ("Welcome to heads up no limit hold'em!")
	play_hand(player, ai, True)



#tests to be deleted
def tests():
	#play_game()
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

tests()


