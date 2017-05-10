import random
from random import randint
import collections
from AIEvaluate import *

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
		self.money = 10000

	def get_money(self):
		return self.money

	def set_money(self,amount):
		self.money = amount

class AI:
	def __init__(self):
		self.money = 10000

	def get_money(self):
		return self.money

	def set_money(self,amount):
		self.money = amount

def preflopHand(card1,card2):
	suited = 'o'
	if card1.suit is card2.suit:
		suited = 's'
	if (card1.num_value() > card2.num_value()):
		return card1.value + card2.value + suited
	else:
		return card2.value + card1.value + suited
def preflopHandRank(hand):
	f = open("Preflop_strength_chart.txt",'r')
	for i in range(0,170):
		line = f.readline()
		if hand in line:
			return line.split('	')[0]
	print (hand)
	

def postFlopHandValue(hole_cards,table_cards):
	#the x's are bc the function also return an array of the relevent card value
	straightFlush,   x = checkStraightFlush(hole_cards,table_cards)
	quads,           x = checkFourOfAKind(hole_cards,table_cards)
	fullHouse,       x = checkFullHouse(hole_cards,table_cards)
	flush,           x = checkFlush(hole_cards,table_cards)
	straight,        x = checkStraight(hole_cards,table_cards)
	setThree,        x = checkSetThree(hole_cards,table_cards)
	tripThree,       x = checkTripThree(hole_cards,table_cards)
	threeOfAKind,    x = checkThreeOfAKind(hole_cards,table_cards)
	twoPair,         x = checkTwoPair(hole_cards,table_cards)
	overPair,        x = checkOverPair(hole_cards,table_cards)
	highPair,        x = checkHighPair(hole_cards,table_cards)
	flushDraw,       x = checkFlushDraw(hole_cards,table_cards)
	openEnder,       x = checkOpenEnder(hole_cards,table_cards)
	gutShot,         x = checkGutShot(hole_cards,table_cards)
	middlePair,      x = checkMiddlePair(hole_cards,table_cards)
	lowPair,         x = checkLowPair(hole_cards,table_cards)
	underPair,       x = checkUnderPair(hole_cards,table_cards)
	highKicker,      x = checkHighKicker(hole_cards,table_cards)
	goodKicker,      x = checkGoodKicker(hole_cards,table_cards)
	backdoorFlush,   x = checkBackdoorFlush(hole_cards,table_cards)
	backdoorStraight,x = checkBackdoorStraight(hole_cards,table_cards)

	hand_value = 0
	if backdoorStraight:
		hand_value += 1
	if backdoorFlush:
		hand_value += 1
	if highKicker:
		hand_value += 5
	elif goodKicker:
		hand_value += 3
	if underPair:
		hand_value += 7
	if lowPair:
		hand_value += 8
	if middlePair:
		hand_value += 12
	if highPair and highKicker:
		hand_value += 20
	elif highPair and goodKicker:
		hand_value += 18
	elif highPair:
		hand_value +=16
	if gutShot:
		hand_value += 6
	if openEnder:
		hand_value += 12
	if flushDraw:
		hand_value += 14
	if overPair:
		hand_value += 25
	if twoPair:
		hand_value += 30
	if tripThree:
		hand_value += 40
	if setThree:
		hand_value +=50
	if straight:
		hand_value += 55
	if flush:
		hand_value += 60
	if fullHouse:
		hand_value += 70
	if quads:
		hand_value += 80
	if straightFlush: 
		hand_value += 100

	return hand_value

def TurnHandValue(hole_cards,table_cards):
	#the x's are bc the function also return an array of the relevent card value
	straightFlush,   x = checkStraightFlush(hole_cards,table_cards)
	quads,           x = checkFourOfAKind(hole_cards,table_cards)
	fullHouse,       x = checkFullHouse(hole_cards,table_cards)
	flush,           x = checkFlush(hole_cards,table_cards)
	straight,        x = checkStraight(hole_cards,table_cards)
	setThree,        x = checkSetThree(hole_cards,table_cards)
	tripThree,       x = checkTripThree(hole_cards,table_cards)
	threeOfAKind,    x = checkThreeOfAKind(hole_cards,table_cards)
	twoPair,         x = checkTwoPair(hole_cards,table_cards)
	overPair,        x = checkOverPair(hole_cards,table_cards)
	highPair,        x = checkHighPair(hole_cards,table_cards)
	flushDraw,       x = checkFlushDraw(hole_cards,table_cards)
	openEnder,       x = checkOpenEnder(hole_cards,table_cards)
	gutShot,         x = checkGutShot(hole_cards,table_cards)
	middlePair,      x = checkMiddlePair(hole_cards,table_cards)
	lowPair,         x = checkLowPair(hole_cards,table_cards)
	underPair,       x = checkUnderPair(hole_cards,table_cards)
	highKicker,      x = checkHighKicker(hole_cards,table_cards)
	goodKicker,      x = checkGoodKicker(hole_cards,table_cards)

	hand_value = 0
	if highKicker:
		hand_value += 3
	elif goodKicker:
		hand_value += 1
	if underPair:
		hand_value += 5
	if lowPair:
		hand_value += 6
	if middlePair:
		hand_value += 10
	if highPair and highKicker:
		hand_value += 20
	elif highPair and goodKicker:
		hand_value += 16
	elif highPair:
		hand_value +=14
	if gutShot:
		hand_value += 4
	if openEnder:
		hand_value += 8
	if flushDraw:
		hand_value += 8
	if overPair:
		hand_value += 24
	if twoPair:
		hand_value += 28
	if tripThree:
		hand_value += 40
	if setThree:
		hand_value +=50
	if straight:
		hand_value += 55
	if flush:
		hand_value += 60
	if fullHouse:
		hand_value += 70
	if quads:
		hand_value += 80
	if straightFlush: 
		hand_value += 100

def riverHandValue(hole_cards,table_cards):
	#the x's are bc the function also return an array of the relevent card value
	straightFlush,   x = checkStraightFlush(hole_cards,table_cards)
	quads,           x = checkFourOfAKind(hole_cards,table_cards)
	fullHouse,       x = checkFullHouse(hole_cards,table_cards)
	flush,           x = checkFlush(hole_cards,table_cards)
	straight,        x = checkStraight(hole_cards,table_cards)
	setThree,        x = checkSetThree(hole_cards,table_cards)
	tripThree,       x = checkTripThree(hole_cards,table_cards)
	threeOfAKind,    x = checkThreeOfAKind(hole_cards,table_cards)
	twoPair,         x = checkTwoPair(hole_cards,table_cards)
	overPair,        x = checkOverPair(hole_cards,table_cards)
	highPair,        x = checkHighPair(hole_cards,table_cards)
	middlePair,      x = checkMiddlePair(hole_cards,table_cards)
	lowPair,         x = checkLowPair(hole_cards,table_cards)
	underPair,       x = checkUnderPair(hole_cards,table_cards)
	highKicker,      x = checkHighKicker(hole_cards,table_cards)
	goodKicker,      x = checkGoodKicker(hole_cards,table_cards)

	hand_value = 0
	if highKicker:
		hand_value += 3
	elif goodKicker:
		hand_value += 1
	if underPair:
		hand_value += 5
	if lowPair:
		hand_value += 6
	if middlePair:
		hand_value += 10
	if highPair and highKicker:
		hand_value += 20
	elif highPair and goodKicker:
		hand_value += 16
	elif highPair:
		hand_value +=14
	if overPair:
		hand_value += 24
	if twoPair:
		hand_value += 28
	if tripThree:
		hand_value += 40
	if setThree:
		hand_value +=50
	if straight:
		hand_value += 55
	if flush:
		hand_value += 60
	if fullHouse:
		hand_value += 70
	if quads:
		hand_value += 80
	if straightFlush: 
		hand_value += 100


def postFlopBoardScare(table_cards):
	
	table_card_values = []
	for x in table_cards:
		table_card_values.append(x.num_value())

	table_card_values.sort()

	flush3 = False
	flush2 = False
	straight3 = False
	straight4 = False
	straight5 = False
	triple = False
	double = False

	if (table_cards[0].suit == table_cards[1].suit and table_cards[1].suit == table_cards[2].suit):
		flush3 = True
	elif table_cards[0].suit is table_cards[1].suit or table_cards[1].suit is table_cards[2].suit or table_cards[0].suit is table_cards[2].suit:
		flush2 = True

	if table_cards[0].value is table_cards[1].value and table_cards[1].value is table_cards[2].value:
		triple = True
	elif table_cards[0].value is table_cards[1].value or table_cards[1].value is table_cards[2].value or table_cards[0].value is table_cards[2].value:
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
	first = first
	player_money = plm
	ai_money = aim
	pot = 0
	player_call = False
	ai_call = False
	current_bet = 0
	bet_number = 1
	ai_num = int(preflopHandRank(preflopHand(ai_cards[0],ai_cards[1])))
	player_wins = False
	ai_wins = False
	agg = 0

	print ('Each player places their $100 ante')
	player_money -= 100
	ai_money -= 100
	pot += 200

	if first and bet_number is 1:
		print ('\n you bet first. To check just bet $0 ')

	while not player_call or not ai_call:
		if first:
			player_call = True
			first = False
			while True:
				print ("The current_bet it : $" + str(current_bet))
				var = raw_input("Please type how much you want to bet or type '-1' to fold ")
				if str(var) is 'fold' or str(var) is 'Fold' or str(var) is 'FOLD' or str(var) is 'F' or str(var) is 'f' or int(var) is -1:
					player_call =True
					ai_call = True
					ai_money += pot
					print ('The AI won the pot')
					ai_wins = True
					#more ai win stuff
					break
				elif int(var) == current_bet:
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
					current_bet = int(var) - current_bet
					player_money = player_money - int(var)
					pot = pot + int(var)
					agg = 1
					break
			bet_number += 1
		else: 
			ai_call = True
			First = True
			if bet_number is 2 and current_bet is 0: 
				#print ('REMOVE THIS: AI num is: ' + str(ai_num))
				r = randint(0,99)
				#print ('REMOVE THIS: r is: ' + str(r))
				if ai_num > 140:
					if r <= 41:
						first = True
						bet = 0
						if r <14:
							bet = 100
						elif r < 28:
							bet = 200
						else:
							bet = 300
						bet = min(bet,ai_money)
						ai_money -= bet
						pot += bet 
						player_call = False
						ai_call = True
						current_bet = bet
						print ('The AI bets: $' +str(bet))
					else:
						first = True
						ai_call = True
						print ('The AI checks')
				elif ai_num >= 120:
					if r <= 60:
						first = True
						bet = 0
						if r <20:
							bet = 100
						elif r < 40:
							bet = 200
						else:
							bet = 300
						bet = min(bet,ai_money)
						ai_money -= bet
						pot += bet 
						player_call = False
						ai_call = True
						current_bet = bet
						print ('The AI bets: $' +str(bet))
					else:
						first = True
						ai_call = True
						print ('The AI checks')
				elif ai_num >= 100:
					if r <= 60:
						first = True
						bet = 0
						if r <20:
							bet = 100
						elif r < 40:
							bet = 200
						else:
							bet = 300
						bet = min(bet,ai_money)
						ai_money -= bet
						pot += bet 
						player_call = False
						ai_call = True
						current_bet = bet
						print ('The AI bets: $' +str(bet))
					else:
						first = True
						ai_call = True
						print ('The AI checks')
				elif ai_num >= 60:
					if r <= 70:
						first = True
						bet = 0
						if r <25:
							bet = 100
						elif r < 50:
							bet = 200
						else:
							bet = 300
						bet = min(bet,ai_money)
						ai_money -= bet
						pot += bet 
						player_call = False
						ai_call = True
						current_bet = bet
						print ('The AI bets: $' +str(bet))
					else:
						first = True
						ai_call = True
						print ('The AI checks')
				elif ai_num >= 30:
					if r <= 90:
						first = True
						bet = 0
						if r <20:
							bet = 100
						elif r < 50:
							bet = 200
						else:
							bet = 300
						bet = min(bet,ai_money)
						ai_money -= bet
						pot += bet 
						player_call = False
						ai_call = True
						current_bet = bet
						print ('The AI bets: $' +str(bet))
					else:
						first = True
						ai_call = True
						print ('The AI checks')
				elif ai_num >= 4:
					if r <= 100:
						first = True
						bet = 0
						if r <20:
							bet = 100
						elif r < 40:
							bet = 200
						else:
							bet = 300
						bet = min(bet,ai_money)
						ai_money -= bet
						pot += bet 
						player_call = False
						ai_call = True
						current_bet = bet
						print ('The AI bets: $' +str(bet))
					else:
						first = True
						ai_call = True
						print ('The AI checks')
				else:
					if r <= 100:
						first = True
						bet = 0
						if r < 30:
							bet = 200
						else:
							bet = 300
						bet = min(bet,ai_money)
						ai_money -= bet
						pot += bet 
						player_call = False
						ai_call = True
						current_bet = bet
						print ('The AI bets: $' +str(bet))
					else:
						first = True
						ai_call = True
						print ('The AI checks')
			elif bet_number is 1:
				#print ('REMOVE THIS: AI num is: ' + str(ai_num))
				r = randint(0,99)
				#print ('REMOVE THIS: r is: ' + str(r))
				if ai_num > 140:
					if r < 3:
						first = True
						bet = min((r+1)*100,ai_money)
						if bet == 300:
							bet = 200
						ai_money -= bet
						pot += bet 
						player_call = False
						ai_call = True
						current_bet = bet
						agg = 1
						print ('The AI bets: $' +str(bet))
					else:
						first = True
						ai_call = True
						print ('The AI checks')
				elif ai_num >= 120:
					if r <= 41:
						first = True
						bet = 0
						if r <20:
							bet = 100
						elif r < 39:
							bet = 200
						else:
							bet = 300
						agg = 1
						bet = min(bet,ai_money)
						ai_money -= bet
						pot += bet 
						player_call = False
						ai_call = True
						current_bet = bet
						print ('The AI bets: $' +str(bet))
					else:
						first = True
						ai_call = True
						print ('The AI checks')
				elif ai_num >= 100:
					if r <= 50:
						first = True
						bet = 0
						if r <15:
							bet = 100
						elif r < 42:
							bet = 200
						else:
							bet = 300
						agg = 1
						bet = min(bet,ai_money)
						ai_money -= bet
						pot += bet 
						player_call = False
						ai_call = True
						current_bet = bet
						print ('The AI bets: $' +str(bet))
					else:
						first = True
						ai_call = True
						print ('The AI checks')
				elif ai_num >= 60:
					if r <= 70:
						first = True
						bet = 0
						if r <25:
							bet = 100
						elif r < 50:
							bet = 200
						else:
							bet = 300
						agg = 1
						bet = min(bet,ai_money)
						ai_money -= bet
						pot += bet 
						player_call = False
						ai_call = True
						current_bet = bet
						print ('The AI bets: $' +str(bet))
					else:
						first = True
						ai_call = True
						print ('The AI checks')
				elif ai_num >= 30:
					if r <= 90:
						first = True
						bet = 0
						if r <20:
							bet = 100
						elif r < 50:
							bet = 200
						else:
							bet = 300
						agg = 1
						bet = min(bet,ai_money)
						ai_money -= bet
						pot += bet 
						player_call = False
						ai_call = True
						current_bet = bet
						print ('The AI bets: $' +str(bet))
					else:
						first = True
						ai_call = True
						print ('The AI checks')
				elif ai_num >= 4:
					if r <= 100:
						first = True
						bet = 0
						if r <20:
							bet = 100
						elif r < 40:
							bet = 200
						else:
							bet = 300
						agg = 1
						bet = min(bet,ai_money)
						ai_money -= bet
						pot += bet 
						player_call = False
						ai_call = True
						current_bet = bet
						print ('The AI bets: $' +str(bet))
					else:
						first = True
						ai_call = True
						print ('The AI checks')
				else:
					if r <= 100:
						first = True
						bet = 0
						if r < 30:
							bet = 200
						else:
							bet = 300
						bet = min(bet,ai_money)
						ai_money -= bet
						pot += bet 
						player_call = False
						ai_call = True
						agg = 1
						current_bet = bet
						print ('The AI bets: $' +str(bet))
					else:
						first = True
						ai_call = True
						print ('The AI checks')
			elif bet_number is 2 and current_bet <= 60:
				#print ('REMOVE THIS: AI num is: ' + str(ai_num))
				r = randint(0,99)
				#print ('REMOVE THIS: r is: ' + str(r))
				if ai_num > 85:
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI calls')
				elif ai_num > 30:
					if r < 50:
						first = True
						ai_money -= (current_bet + 250)
						pot += (current_bet + 250)
						current_bet = 250
						player_call = False
						print ('AI raises it an additional $250')
					else:
						first = True
						ai_money -= current_bet
						pot += current_bet
						ai_call = True
						print ('AI calls')
				else:
					first = True
					ai_money -= (current_bet + 250)
					pot += (current_bet + 250)
					current_bet = 250
					player_call = False
					print ('AI raises it an additional $250')
			elif bet_number is 2:
				#print ('REMOVE THIS: AI num is: ' + str(ai_num))
				r = randint(0,99)
				#print ('REMOVE THIS: r is: ' + str(r))
				if ai_num > 130:
					print('AI folds you win this hand')
					player_wins = True
					player_money += pot
					ai_call = True
				elif ai_num > 90:
					if current_bet > 300 or r < 50:
						print('AI folds you win this hand')
						player_wins = True
						player_money += pot
						ai_call = True
					else:
						first = True
						ai_money -= current_bet
						pot += current_bet
						ai_call = True
						print ('AI calls')
				elif ai_num > 30:
					if current_bet > 700:
						print('AI folds you win this hand')
						player_wins = True
						player_money += pot
						ai_call = True
					elif current_bet <= 300 and r <30:
						first = True
						bet = pot
						ai_money -= (current_bet + bet)
						pot += (current_bet + bet)
						current_bet = bet
						player_call = False
						print ('AI raises it an additional $' + bet)
					else:
						first = True
						ai_money -= current_bet
						pot += current_bet
						ai_call = True
						print ('AI calls')
				elif ai_num > 4: 
					if current_bet < 1100 and r <80:
						first = True
						bet = pot
						ai_money -= (current_bet + bet)
						pot += (current_bet + bet)
						current_bet = bet
						player_call = False
						print ('AI raises it an additional $' + str(bet))
					else:
						first = True
						ai_money -= current_bet
						pot += current_bet
						ai_call = True
						print ('AI calls')
				else:
					first = True
					bet = pot
					ai_money -= (current_bet + bet)
					pot += (current_bet + bet)
					current_bet = bet
					player_call = False
					print ('AI raises it an additional $' + str(bet))
			elif bet_number is 3 and current_bet <= 300:
				#print ('REMOVE THIS: AI num is: ' + str(ai_num))
				r = randint(0,99)
				if (current_bet >60 and ai_num >= 100):
					print('AI folds you win this hand')
					player_wins = True
					player_money += pot
					ai_call = True
				elif ai_num > 60 or (ai_num > 4 and r < 50):
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI calls')
				else:
					first = True
					bet = pot
					ai_money -= (current_bet + bet)
					pot += (current_bet + bet)
					current_bet = bet
					player_call = False
					print ('AI raises it an additional $' + str(bet))
			elif bet_number is 3:
				r = randint(0,99)
				if ai_num > 130 or (ai_num > 100 and r > 50) or (ai_num>70 and current_bet >= 600) or (ai_num>40 and current_bet > 1000):
					print('AI folds you win this hand')
					player_wins = True
					player_money += pot
					ai_call = True
				elif ai_num < 8:
					first = True
					bet = pot
					ai_money -= (current_bet + bet)
					pot += (current_bet + bet)
					current_bet = bet
					player_call = False
					print ('AI raises it an additional $' + str(bet))
				else:
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI calls')
			elif bet_number is 4:
				r = randint(0,99)
				if ai_num <=3 and r < 50:
					first = True
					bet = min (player_money,ai_money)
					ai_money -= (current_bet + bet)
					pot += (current_bet + bet)
					current_bet = bet
					player_call = False
					print ('AI raises it an additional $' + str(bet))
				elif current_bet >= 1000 and ai_num > 40:
					print('AI folds you win this hand')
					player_wins = True
					player_money += pot
					ai_call = True
				else:
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI calls')
			else:
				r = randint(0,99)	
				if ai_num <=2 and r < 50:
					first = True
					bet = min (player_money,ai_money)
					ai_money -= (current_bet + bet)
					pot += (current_bet + bet)
					current_bet = bet
					player_call = False
					print ('AI raises it an additional $' + str(bet))
				elif current_bet >= 800 and ai_num > 5:
					print('AI folds you win this hand')
					player_wins = True
					player_money += pot
					ai_call = True
				else:
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI calls')
		bet_number += 1
	#return [Player wins, AI wins, pot, player_money, ai_money, aggretion level]
	if bet_number == 2 and agg == 1:
		bet_number =3
	return [player_wins, ai_wins,pot, player_money, ai_money, bet_number - 2]


def play_flop(player_money,ai_money,first,player_cards,ai_cards,table_cards,pot,aggretion):
	first = first
	player_money = player_money
	ai_money = ai_money
	pot = pot
	player_call = False
	ai_call = False
	current_bet = 0
	bet_number = 1
	player_wins = False
	ai_wins = False
	aggretion = aggretion
	value = postFlopHandValue(ai_cards,table_cards)
	scare = postFlopBoardScare(table_cards)
	aggretion = 0

	if first and bet_number is 1:
		print ('\n You bet the flop first. To check just bet $0 ')

	while not player_call or not ai_call:
		if first:
			player_call = True
			first = False
			while True:
				print ("The current_bet is : $" + str(current_bet))
				var = raw_input("Please type how much you want to bet or type '-1' to fold ")
				if str(var) is 'fold' or str(var) is 'Fold' or str(var) is 'FOLD' or str(var) is 'F' or str(var) is 'f' or int(var) is -1:
					player_call =True
					ai_call = True
					ai_money += pot
					print ('The AI won the pot')
					ai_wins = True
					#more ai win stuff
					break
				elif int(var) == current_bet:
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
					current_bet = int(var) - current_bet
					player_money = player_money - int(var)
					pot = pot + int(var)
					aggretion += 1
					if current_bet >= (pot-current_bet)*2/5:
						aggretion +=1
					if current_bet >= (pot-current_bet)*3/5 and current_bet > 400:
						aggretion += 1
					if current_bet >= (pot-current_bet) and current_bet > 700:
						aggretion += 1
					break
			bet_number += 1
		else:
			r = randint(0,99)
			ai_call = True
			First = True
			if bet_number is 1:
				bet_prob = 10 + scare*5 -((aggretion-2)*10)


				if value <= 22:
					bet_prob += (50./22)*value
				else:
					bet_prob = 50
				bet_prob = int(bet_prob)
				if (r>bet_prob):
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI checks')
				else:
					first = True
					bet = min (ai_money, max(int(pot/2)-150,300))
					aggretion = 2
					ai_money -= (current_bet + bet)
					pot += (current_bet + bet)
					current_bet = bet
					player_call = False
					print ('AI raises it an additional $' + str(bet))
			elif bet_number is 2 and current_bet is 0:
				bet_prob = 30 + scare*5 -((aggretion-2)*10)
				if value <= 22:
					bet_prob += (50/22)*value
				else:
					bet_prob = 80
				bet_prob = int(bet_prob)
				if (r>bet_prob):
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI checks')
				else:
					first = True
					bet = min (ai_money, max(int(pot/2)-120,300))
					aggretion = 2
					ai_money -= (current_bet + bet)
					pot += (current_bet + bet)
					current_bet = bet
					player_call = False
					print ('AI raises it an additional $' + str(bet))
			elif bet_number is 2 or 3:
				percent_of_pot = current_bet/(pot-current_bet)
				bet_prob = 0

				if value < 16:
					bet_prob += value*4
				else:
					bet_prob = 100
				bet_prob = int(bet_prob)
				if (r>bet_prob):
					print('AI folds you win this hand')
					player_wins = True
					player_money += pot
					ai_call = True
				else:
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI calls')
			elif bet_number is 4:
				percent_of_pot = current_bet/(pot-current_bet)
				bet_prob = 0
				if value < 17:
					bet_prob = 0 
				elif value < 20:
					bet_prob += value*3
				else:
					bet_prob = 100
				bet_prob = int(bet_prob)
				if (r>bet_prob):
					print('AI folds you win this hand')
					player_wins = True
					player_money += pot
					ai_call = True
				else:
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI calls')
				aggretion = 4
			bet_number += 1

	return [player_wins, ai_wins, pot, player_money, ai_money, aggretion]


def play_turn(player_money,ai_money,first,player_cards,ai_cards,table_cards,pot,aggretion):
	first = first
	player_money = player_money
	ai_money = ai_money
	pot = pot
	player_call = False
	ai_call = False
	current_bet = 0
	bet_number = 1
	player_wins = False
	ai_wins = False
	aggretion = aggretion
	value = postFlopHandValue(ai_cards,table_cards)
	aggretion = 0

	if first and bet_number is 1:
		print ('\n You bet the flop first. To check just bet $0 ')

	while not player_call or not ai_call:
		if first:
			player_call = True
			first = False
			while True:
				print ("The current_bet is : $" + str(current_bet))
				var = raw_input("Please type how much you want to bet or type '-1' to fold ")
				if str(var) is 'fold' or str(var) is 'Fold' or str(var) is 'FOLD' or str(var) is 'F' or str(var) is 'f' or int(var) is -1:
					player_call =True
					ai_call = True
					ai_money += pot
					print ('The AI won the pot')
					ai_wins = True
					#more ai win stuff
					break
				elif int(var) == current_bet:
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
					current_bet = int(var) - current_bet
					player_money = player_money - int(var)
					pot = pot + int(var)
					aggretion += 1
					if current_bet >= (pot-current_bet)*2/5:
						aggretion +=1
					if current_bet >= (pot-current_bet)*3/5 and current_bet > 400:
						aggretion += 1
					if current_bet >= (pot-current_bet) and current_bet > 700:
						aggretion += 1
					break
			bet_number += 1
		else:
			r = randint(0,99)
			ai_call = True
			First = True
			if bet_number is 1:
				bet_prob = 20 -((aggretion-2)*20)

				if value <= 15:
					bet_prob -= 10
				if value <= 30:
					bet_prob += (20./22)*value
				else:
					bet_prob = 70
				bet_prob = int(bet_prob)
				if (r>bet_prob):
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI checks')
				else:
					first = True
					bet = int(min (ai_money, max(int(pot*2/5)+150,300)))
					aggretion = 2
					ai_money -= (current_bet + bet)
					pot += (current_bet + bet)
					current_bet = bet
					player_call = False
					print ('AI raises it an additional $' + str(bet))
			elif bet_number is 2 and current_bet is 0:
				bet_prob = 40 -((aggretion-2)*20)

				if value <= 15:
					bet_prob -= 20
				if value <= 30:
					bet_prob += (30./22)*value
				else:
					bet_prob = 70
				bet_prob = int(bet_prob)
				if (r>bet_prob):
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI checks')
				else:
					first = True
					bet = int(min (ai_money, max(int(pot*2/5)+150,300)))
					aggretion = 2
					ai_money -= (current_bet + bet)
					pot += (current_bet + bet)
					current_bet = bet
					player_call = False
					print ('AI raises it an additional $' + str(bet))
			elif bet_number is 2 or 3:
				percent_of_pot = current_bet/(pot-current_bet)
				bet_prob = 0

				if value < 25:
					bet_prob += value*4
				else:
					bet_prob = 100
				bet_prob = int(bet_prob)
				if (r>bet_prob):
					print('AI folds you win this hand')
					player_wins = True
					player_money += pot
					ai_call = True
				else:
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI calls')
			elif bet_number is 4:
				percent_of_pot = current_bet/(pot-current_bet)
				bet_prob = 0
				if value < 17:
					bet_prob = 0 
				elif value < 16:
					bet_prob = 0
				elif value < 30:
					bet_prob += value*3.5
				else:
					bet_prob = 100
				bet_prob = int(bet_prob)
				if (r>bet_prob):
					print('AI folds you win this hand')
					player_wins = True
					player_money += pot
					ai_call = True
				else:
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI calls')
				aggretion = 4
			bet_number += 1

	return [player_wins, ai_wins, pot, player_money, ai_money, aggretion]


def play_river(player_money,ai_money,first,player_cards,ai_cards,table_cards,pot,aggretion):
	first = first
	player_money = player_money
	ai_money = ai_money
	pot = pot
	player_call = False
	ai_call = False
	current_bet = 0
	bet_number = 1
	player_wins = False
	ai_wins = False
	aggretion = aggretion
	value = postFlopHandValue(ai_cards,table_cards)
	aggretion = 0

	if first and bet_number is 1:
		print ('\n You bet the flop first. To check just bet $0 ')

	while not player_call or not ai_call:
		if first:
			player_call = True
			first = False
			while True:
				print ("The current_bet is : $" + str(current_bet))
				var = raw_input("Please type how much you want to bet or type '-1' to fold ")

				if int(var) == -1:
					player_call =True
					ai_call = True
					ai_money += pot
					print ('The AI won the pot')
					ai_wins = True
					#more ai win stuff
					break
				elif int(var) == current_bet:
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
					current_bet = int(var) - current_bet
					player_money = player_money - int(var)
					pot = pot + int(var)
					aggretion += 1
					if current_bet >= (pot-current_bet)*2/5:
						aggretion +=1
					if current_bet >= (pot-current_bet)*3/5 and current_bet > 400:
						aggretion += 1
					if current_bet >= (pot-current_bet) and current_bet > 700:
						aggretion += 1
					break
			bet_number += 1
		else:
			r = randint(0,99)
			ai_call = True
			First = True
			if bet_number is 1:
				bet_prob = 10 -((aggretion-2)*20)

				if value <= 17:
					bet_prob == 0
				if value <= 30:
					bet_prob += (10./22)*value
				else:
					bet_prob = 100
				bet_prob = int(bet_prob)
				if (r>bet_prob):
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI checks')
				else:
					first = True
					bet = int(min (ai_money, max(int(pot*2/5)+150,300)))
					aggretion = 2
					ai_money -= (current_bet + bet)
					pot += (current_bet + bet)
					current_bet = bet
					player_call = False
					print ('AI raises it an additional $' + str(bet))
			elif bet_number is 2 and current_bet is 0:
				bet_prob = 20 -((aggretion-2)*20)

				if value <= 17:
					bet_prob = 0 
				if value <= 30:
					bet_prob += (30./22)*value
				else:
					bet_prob = 100
				bet_prob = int(bet_prob)
				if (r>bet_prob):
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI checks')
				else:
					first = True
					bet = int(min (ai_money, max(int(pot*2/5)+150,300)))
					aggretion = 2
					ai_money -= (current_bet + bet)
					pot += (current_bet + bet)
					current_bet = bet
					player_call = False
					print ('AI raises it an additional $' + str(bet))
			elif bet_number is 2 or 3:
				percent_of_pot = current_bet/(pot-current_bet)
				bet_prob = 0

				if value < 10:
					bet_prob = 0
				elif value < 18 and aggretion > 2:
					bet_prob = 0
				else:
					bet_prob = 100
				bet_prob = int(bet_prob)
				if value > 45 or r<15:
					bet = min(player_money, int(pot*3/5))
					bet = min(bet,ai_money)
					ai_money -= bet
					pot += bet 
					player_call = False
					ai_call = True
					current_bet = bet
					print ('The AI bets: $' +str(bet))
				elif (r>bet_prob):
					print('AI folds you win this hand')
					player_wins = True
					player_money += pot
					ai_call = True
				else:
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI calls')
			else:
				percent_of_pot = current_bet/(pot-current_bet)
				
				bet_prob = int(bet_prob)

				if (value < 25):
					print('AI folds you win this hand')
					player_wins = True
					player_money += pot
					ai_call = True
				elif (value >= 50):
					bet = min(player_money, int(pot*3/5))
					bet = min(bet,ai_money)
					ai_money -= bet
					pot += bet 
					player_call = False
					ai_call = True
					current_bet = bet
					print ('The AI bets: $' +str(bet))
				else:
					first = True
					ai_money -= current_bet
					pot += current_bet
					ai_call = True
					print ('AI calls')
				aggretion = 4
			bet_number += 1

	return [player_wins, ai_wins, pot, player_money, ai_money, aggretion]


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
	#print('REMOVER THIS LINE: AI has been delt: ' + card2.card() + ' ' + card4.card())
	preflop = play_preflop(player_money,ai_money,first,player_cards,ai_cards)
	player_wins = preflop[0]
	ai_wins = preflop [1]
	pot = preflop[2]
	player_money = preflop[3]
	ai_money = preflop[4]
	aggretion = preflop[5]
	over = player_wins or ai_wins

	if not over:
		print ("\nYou currently have : $" + str(player_money))
		print ("Your apponent has: $" +str(ai_money))
		print ("Pot is currently: " + str(pot))

		card5 = deck.dealCard()
		card6 = deck.dealCard()
		card7 = deck.dealCard()

		table_cards = []
		table_cards.append(card5)
		table_cards.append(card6)
		table_cards.append(card7)

		print ("\nHere comes the flop:")
		print ("The cards on the table are: " + card5.card() + ' ' + card6.card() + ' ' + card7.card())
		print ("Your cards are: " + card1.card() + ' ' + card3.card())


		flop = play_flop(player_money,ai_money,first,player_cards,ai_cards,table_cards,pot,aggretion)

		player_wins = flop[0]
		ai_wins = flop [1]
		pot = flop[2]
		player_money = flop[3]
		ai_money = flop[4]
		aggretion = flop[5]
		over = player_wins or ai_wins

		if not over:
			
			print ("\nYou currently have : $" + str(player_money))
			print ("Your apponent has: $" +str(ai_money))
			print ("Pot is currently: " + str(pot))
			card8 = deck.dealCard()
			table_cards.append(card8)

			print ("\nHere comes the turn:")
			print("The turn card is: " + card8.card())
			print ("The cards on the table are: " + card5.card() + ' ' + card6.card() + ' ' + card7.card() + ' ' + card8.card())
			print ("Your cards are: " + card1.card() + ' ' + card3.card())

			turn = play_turn(player_money,ai_money,first,player_cards,ai_cards,table_cards,pot,aggretion)
			player_wins = turn[0]
			ai_wins = turn [1]
			pot = turn[2]
			player_money = turn[3]
			ai_money = turn[4]
			aggretion = (turn[5]*2 + aggretion)/3.0
			over = player_wins or ai_wins

			if not over: 
				print ("\nYou currently have : $" + str(player_money))
				print ("Your apponent has: $" +str(ai_money))
				print ("Pot is currently: " + str(pot))
				card9 = deck.dealCard()
				table_cards.append(card9)
				print ("\nHere comes the turn:")
				print("The river card is: " + card9.card())
				print ("The cards on the table are: " + card5.card() + ' ' + card6.card() + ' ' + card7.card() + ' ' + card8.card() + ' ' + card9.card())
				print ("Your cards are: " + card1.card() + ' ' + card3.card())

				river = play_river(player_money,ai_money,first,player_cards,ai_cards,table_cards,pot,aggretion)
				player_wins = river[0]
				ai_wins = river [1]
				pot = river[2]
				player_money = river[3]
				ai_money = river[4]
				over = player_wins or ai_wins

				if not over:
					winner = findWinner(ai_cards, player_cards, table_cards)
					print ("\n the AI had " + card2.card() + ' ' + card4.card())
					if winner is 1:
						print ("The AI won a pot of: $" + str(pot))
						ai_money += pot
					elif winner is -1:
						print ("You won a pot of: $" + str(pot))
						player_money += pot
					else:
						print ("split pot")
						player_money += pot/2
						ai_money += pot/2
	player.money = player_money
	ai.money = ai_money
	


def play_game():
	player = Player()
	ai = AI ()
	start = False
	print ("Welcome to heads up no limit hold'em!")
	while (True):
		play_hand(player, ai, start)
		start = not start
		if player.money <= 0:
			print ("You lost :(")
			break
		elif ai.money <=0:
			print ("You won!")
			break







#tests to be deleted
def tests():
	play_game()
	# d = Deck()
	# d.deck()
	# print('')
	# print('')
	# card1 = d.dealCard()
	# card2 = d.dealCard()
	# print('')
	# print('')
	# d.deck()
	# print('')
	# print('')
	# print preflopHand(card1,card2)
	# print preflopHandRank(preflopHand(card1,card2))
	
	""" if you want to see how the evaluate functions work
	return True or False, followed by the best 5 cards only
	guarenteed to work if there is no better type"""
def testevaluaters():
	card1=Card("5",'C')
	card2=Card("4",'C')
	card3=Card("2",'H')
	card4=Card("A",'C')
	card5=Card("3",'C')
	card6=Card("2", 'C')
	card7=Card("3",'C')
	hole_cards=[card1, card2]
	shared_cards=[card3, card4, card5, card6, card7,]
	truth, best_five = checkStraightFlush(hole_cards, shared_cards)
	#truth, best_five = checkFourofAKind(hole_cards, shared_cards)
	#truth, best_five = checkFullHouse(hole_cards, shared_cards)
	#truth, best_five = checkFlush(hole_cards, shared_cards)
	#truth, best_five = checkStraight(hole_cards, shared_cards)
	#truth, best_five = checkThreeOfAKind(hole_cards, shared_cards)
	#truth, best_five = checkTwoPair(hole_cards, shared_cards)
	#truth, best_five = checkOnePair(hole_cards, shared_cards)
	#truth, best_five = checkHighCard(hole_cards, shared_cards)
	
	
	print(truth, best_five)
	

	
def testfindWinner():
	AI_card1=Card("9",'H')
	AI_card2=Card("8",'D')
	
	Player_card1=Card("3",'D')
	Player_card2=Card("J",'H')
	
	card3=Card("K",'C')
	card4=Card("5",'C')
	card5=Card("2",'H')
	card6=Card("Q", 'C')
	card7=Card("4",'C')
	
	AI_cards=[AI_card1, AI_card2]
	Player_cards=[Player_card1, Player_card2]
	shared_cards=[card3, card4, card5, card6, card7,]
	winner=findWinner(AI_cards, Player_cards, shared_cards)
	print(winner)

	
#tests()
#testevaluaters()

play_game()
	