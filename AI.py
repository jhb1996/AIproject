#!/usr/bin/env python3
import random
import collections


def getIndex(card):
    rank=card[0]
    if rank=='J':
        index=9*4
    elif rank=='Q':
        index=10*4
    elif rank=='K':
        index=11*4
    elif rank=='A':
        index=12*4
    else:
        index=(int(rank)-2)*4
    
    suit=card[1]
    if suit=='h':
        index=index+0
    if suit=='c':
        index=index+1
    if suit=='s':
        index=index+2
    if suit=='d':
        index=index+3

    ranks=['2','3','4','5','6','7','8','9','T','J', 'Q', 'K', 'A']
    suits=['h', 'c', 's', 'd']
    
    return index

"""these methods all request cards on the command line and return them as well as remove them from the deck"""
def requestHoleCards():
    input_var = input("Please Deal 2 cards (input must be a card number followed by its suit letter followed by a second number followed by its suit. No Spaces!!!)")
    print(input_var[0:2])
    print(getIndex(input_var[0:2]))
    Deck[getIndex(input_var[0:2])]=False
    
    print(input_var[2:4])
    Deck[getIndex(input_var[2:4])]=False
    print(Deck)
    return input_var

def requestFlop():
    input_var = input("Please Deal 3 cards (input must be a card number followed by its suit's first letter etc. NO SPACES")
    Deck[getIndex(input_var[0:2])]=False
    Deck[getIndex(input_var[2:4])]=False
    Deck[getIndex(input_var[4:6])]=False
    return input_var

def requestTurn():
    input_var = input("Please Deal 1 cards (input must be a card number followed by its suit's first letter")
    Deck[getIndex(input_var)]=False
    return input_var

def requestRiver():
    input_var = input("Please Deal 1 cards (input must be a card number followed by its suit's first letter")
    Deck[getIndex(input_var)]=False
    return input_var

def requestShow():
    input_var = input("Please tell me what you have. NO SPACES!!!")
    return input_var

def requestBetCheckOrFold():
    """returns -1 if P2 folds, 0 if P2 checks and betAmount if P2 bets.
    Used only for the first round of betting"""
    global Pot
    global P2money
    input_var = input("bet, check, or fold? (type 'bet' 'check' or 'fold') ")
    if input_var == 'fold':
        return -1
    elif input_var == 'check':
        return 0
    elif input_var== 'bet':
        input_var = int(input("How much? (type a number in quotation marks"))
        Pot=Pot
        P2money=P2money-input_var
        return input_var 

def requestCallRaiseOrFold(betAmount):
    """returns -1 if P2 folds, 0 if P2 calls
    and raiseAmount if P2 raises (raises are the amount on top of the previous bet?)."""
    global Pot
    global P2money
    
    input_var = input("call, raise, or fold? (type 'call' 'raise' or 'fold') ")
    if input_var == 'fold':
        return -1
    elif input_var == 'call':
        Pot=Pot+betAmount
        return 0
    elif input_var== 'raise':
        Pot=Pot+betAmount+input_var
        input_var = int(input("How much? (type a number in quotation marks"))
        P2money=P2money-input_var
        return input_var 
        
        
        
        
def chooseBetCheckOrFoldHole():
    """decides whether to bet check of fold. Used only for betting with no previous bet this round
        Output: AIbetAmount: -1 if AI folds, 0 if AI calls and raiseAmount if AI raises"""

    global Pot
    global AImoney
    global AIHand
    
    #must be implemented
    #set a variable betAmount to be equal to the amount
    betAmount=0 #replace this
    
    #ends with the following 
    Pot=Pot+betAmount
    AImoney=AImoney-betAmount
    return betAmount

def chooseCallRaiseOrFoldHole(betAmount):
    """Decides whether to call raise or fold.
    Input: betAmount: How much the opponent bet/raised
    Output: AIbetAmount: -1 if AI folds, 0 if AI calls and raiseAmount if AI raises"""
    
    global Pot
    global AImoney
    global AIHand
    
    #must be implemented
    #set a variable betAmount to be equal to the amount
    AIbetAmount=0 #replace this
    
    #ends with the following 
    Pot=Pot+AIbetAmount
    AImoney=AImoney-AIbetAmount
    return AIbetAmount

def chooseBetCheckOrFoldFlop():
    """decides whether to bet check of fold. Used only for betting with no previous bet this round
        Output: AIbetAmount: -1 if AI folds, 0 if AI calls and raiseAmount if AI raises"""

    global Pot
    global AImoney
    global AIHand
    global Flop
    
    #must be implemented
    #set a variable betAmount to be equal to the amount
    betAmount=0 #replace this
    
    #ends with the following 
    Pot=Pot+betAmount
    AImoney=AImoney-betAmount
    return betAmount

def chooseCallRaiseOrFoldFlop(betAmount):
    """Decides whether to call raise or fold.
    Input: betAmount: How much the opponent bet/raised
    Output: AIbetAmount: -1 if AI folds, 0 if AI calls and raiseAmount if AI raises"""
    
    global Pot
    global AImoney
    global AIHand
    global Flop # a string of three cards
    
    #must be implemented
    #set a variable betAmount to be equal to the amount
    AIbetAmount=0 #replace this
    
    #ends with the following 
    Pot=Pot+AIbetAmount
    AImoney=AImoney-AIbetAmount
    return AIbetAmount

def chooseBetCheckOrFoldTurn():
    """decides whether to bet check of fold. Used only for betting with no previous bet this round
        Output: AIbetAmount: -1 if AI folds, 0 if AI calls and raiseAmount if AI raises"""

    global Pot
    global AImoney
    global AIHand
    global Flop
    global Turn
    
    #must be implemented
    #set a variable betAmount to be equal to the amount
    betAmount=0 #replace this
    
    #ends with the following 
    Pot=Pot+betAmount
    AImoney=AImoney-betAmount
    return betAmount

def chooseCallRaiseOrFoldTurn(betAmount):
    """Decides whether to call raise or fold.
    Input: betAmount: How much the opponent bet/raised
    Output: AIbetAmount: -1 if AI folds, 0 if AI calls and raiseAmount if AI raises"""
    
    global Pot
    global AImoney
    global AIHand
    global Flop # a string of three cards
    global Turn
    
    #must be implemented
    #set a variable betAmount to be equal to the amount
    AIbetAmount=0 #replace this
    
    #ends with the following 
    Pot=Pot+AIbetAmount
    AImoney=AImoney-AIbetAmount
    return AIbetAmount

def chooseBetCheckOrFoldRiver():
    """decides whether to bet check of fold. Used only for betting with no previous bet this round
        Output: AIbetAmount: -1 if AI folds, 0 if AI calls and raiseAmount if AI raises"""

    global Pot
    global AImoney
    global AIHand
    global Flop
    global Turn
    global River
    
    #must be implemented
    #set a variable betAmount to be equal to the amount
    betAmount=0 #replace this
    
    #ends with the following 
    Pot=Pot+betAmount
    AImoney=AImoney-betAmount
    return betAmount


def chooseCallRaiseOrFoldRiver(betAmount):
    """Decides whether to call raise or fold.
    Input: betAmount: How much the opponent bet/raised
    Output: AIbetAmount: -1 if AI folds, 0 if AI calls and raiseAmount if AI raises"""
    
    global Pot
    global AImoney
    global AIHand
    global Flop # a string of three cards
    global Turn
    global River
    
    #must be implemented
    #set a variable betAmount to be equal to the amount
    AIbetAmount=0 #replace this
    
    #ends with the following 
    Pot=Pot+AIbetAmount
    AImoney=AImoney-AIbetAmount
    return AIbetAmount

def evaluateRaw():
    """figures out the raw odds (ignoring opponent strategy) of a hand"""
    
    #we can try this in different ways.
    #For the river we can probably run through all posible combinations
    #In general we will probably want to try a monte carlos simulation (play 1000 random games)
    pass

def OpponentBettingPatern():
    """figures out the likelyhood the opponent has good cards by looking at the betting patern"""
    
    pass

def bettingStrategy1():
    pass
def bettingStrategy2():
    pass
def bettingStrategy3():
    pass
def bettingStrategy4():
    pass
def bettingStrategy5():
    pass
def bettingStrategy6():
    pass
def bettingStrategy7():
    pass
def bettingStrategy8():
    pass

def gatherDataHole(P2Hand,AIfirst,P2BetAmountHole, P2MoneyHole):
    """creates a list containing
     [P2 starting cards quality, who went first(bool, True if AI first), #how much did P2 bet, P2money]"""
    return [evaluateRaw(P2Hand), AIfirst, P2BetAmountHole, P2MoneyHole]
    
    
def ante():
    global AImoney
    global P2money
    global Pot
    print (AImoney)
    print("I ante $100")
    AImoney=AImoney-100
    print ("I assume you are anteing as well")
    P2money=P2money-100
    Pot=200

def newDeck():
    ranks=['2','3','4','5','6','7','8','9','T','J', 'Q', 'K', 'A']
    suits=['h', 'c', 's', 'd']
    deck=[]
    for i in ranks:
         for j in suits:
            deck.append(i+j)
        
    return deck


def declareWinner(): #not yet implemented
    """returns the winner of the hand
    output: 1 if AI wins, -1 if P2 wins, 0 if Tie
    """
    
    global AIHand
    global Flop
    global Turn
    global River
    
    #search through best possible hands in order
    return(0)#placeholder
    
def allocatePot(winner):
    global Pot
    global AImoney
    global P2money
    
    if winner==1:
        AImoney=AImoney+Pot
        print("I won ", Pot, " I now have ", AImoney, " dollars" )
        print("You lost ", Pot, " You now have ", P2money, " dollars" )

    elif winner==-1:
        P2money=P2money+Pot
        print("I lost ", Pot, " I now have ", AImoney, " dollars" )
        print("You won ", Pot, " You now have ", P2money, " dollars" )
    else: #winner==0:
        AImoney=AImoney+Pot/2
        P2money=P2money+Pot/2
        print("We split ", Pot, " I now have ", AImoney, " dollars" )
        print(" You now have ", P2money, " dollars" )
    Pot=0
    
def play():
    #initialize values. Only done on first hand.
    
    global AIturn
    AIturn=True
    global AImoney
    AImoney=25000
    global P2money
    P2money=2500
    global Pot
    Pot=0
    global Deck
    Deck=[]
    print("I go first")
    global AIhand
    global Flop
    global Turn
    global River
    global CurrentGameHistory
    CurrentGame=[]
    
    # loop runs until one player runs out of money
    while AImoney > 0 and P2money > 0:
        Deck=newDeck()
        fold=False
        ante() #deducts $100 from both players and adds it to the pot

        """The hold cards"""
        AIhand=requestHoleCards()
        betting=True
        AIfirst=AIturn#used for data gathering
        P2MoneyHole=P2money
        #if AI bets first, request an action from the AI, if the AI checks then request a bet from P2
        if AIturn==True:
            AIBetAmount = chooseBetCheckOrFoldHole() #must be implemented
            if AIBetAmount==-1: #if the AI folds
                betting=False
                fold=True
            elif AIBetAmount==0:
                AIturn=not AIturn
                P2BetAmount=requestBetCheckOrFold()
                if P2BetAmount==-1: #if P2 folds
                    betting=False
                    fold=True
                elif P2BetAmount==0:
                    betting=False
        #if P2 bets first, request an action from P2, if P2 checks then request a bet from the AI                
        else:
            P2BetAmount = requestBetCheckOrFold()
            if P2BetAmount==-1: #if P2 folds
                betting=False
                fold=True
            elif P2BetAmount==0:
                AIturn=not AIturn
                AIBetAmount = chooseBetCheckOrFoldHole()
                if AIBetAmount==-1: #if the AI folds
                    betting=False
                    fold=True
                elif AIbetAmount==0:
                        betting=False
        
        AIturn=not AIturn
        P2BetAmountHole=P2BetAmount
        
        while betting==True: #while one player can still bet
            if AIturn==True:
                AIBetAmount = chooseCallRaiseOrFoldHole(P2BetAmount)
                if AIBetAmount==-1: #if the AI folds
                    betting=False
                    fold=True
                elif AIBetAmount==0: #if AI calls
                    betting=False
            else:
                P2BetAmount = requestBetCheckOrFold(AIBetAmount)
                if P2BetAmount==-1: #if P2 folds
                    betting=False
                    fold=True
                elif P2BetAmount==0:
                    betting=False
            AIturn=not AIturn
        
        """The flop"""    
        if fold==False:
            Flop=requestFlop()
            betting=True
        
            #if AI bets first, request an action from the AI, if the AI checks then request a bet from P2
            if AIturn==True:
                AIBetAmount = chooseBetCheckOrFoldFlop() #must be implemented
                if AIBetAmount==-1: #if the AI folds
                    betting=False
                    fold=True
                elif AIBetAmount==0:#if the AI checks
                    AIturn=not AIturn
                    P2BetAmount=requestBetCheckOrFold()
                    if P2BetAmount==-1: #if P2 folds
                        betting=False
                        fold=True
                    elif P2BetAmount==0:#if P2(ie both players check)
                        betting=False
            #if P2 bets first, request an action from P2, if P2 checks then request a bet from the AI                
            else:
                P2BetAmount = requestBetCheckOrFold()
                if P2BetAmount==-1: #if P2 folds
                    betting=False
                    fold=True
                elif P2BetAmount==0:
                    AIturn=not AIturn
                    AIBetAmount = chooseBetCheckOrFoldFlop()
                    if AIBetAmount==-1: #if the AI folds
                        betting=False
                        fold=True
                    elif AIBetAmount==0:#if AI(ie both players check)
                            betting=False
            AIturn=not AIturn
            
            P2BetAmountFlop=P2BetAmount
            
            while betting==True: #while one player can still bet
                if AIturn==True:
                    AIBetAmount = chooseCallRaiseOrFoldFlop(P2BetAmount)
                    if AIBetAmount==-1: #if the AI folds
                        betting=False
                        fold=True
                    elif AIBetAmount==0: #if AI calls
                        betting=False
                else:
                    P2BetAmount = requestBetCheckOrFold(AIBetAmount)
                    if P2BetAmount==-1: #if P2 folds
                        betting=False
                        fold=True
                    elif P2BetAmount==0:
                        betting=False
                AIturn=not AIturn
            
        """The turn"""    
        if fold==False:
            Turn=requestTurn()
            betting=True
        
            #if AI bets first, request an action from the AI, if the AI checks then request a bet from P2
            if AIturn==True:
                AIBetAmount = chooseBetCheckOrFoldTurn() #must be implemented
                if AIBetAmount==-1: #if the AI folds
                    betting=False
                    fold=True
                elif AIBetAmount==0:
                    AIturn=not AIturn
                    P2BetAmount=requestBetCheckOrFold()
                    if P2BetAmount==-1: #if P2 folds
                        betting=False
                        fold=True
                    elif P2BetAmount==0:
                        betting=False
            #if P2 bets first, request an action from P2, if P2 checks then request a bet from the AI                
            else:
                P2BetAmount = requestBetCheckOrFold()
                if P2BetAmount==-1: #if P2 folds
                    betting=False
                    fold=True
                elif P2BetAmount==0:
                    AIturn=not AIturn
                    AIBetAmount = chooseBetCheckOrFoldFlopTurn()
                    if AIBetAmount==-1: #if the AI folds
                        betting=False
                        fold=True
                    elif AIbetAmount==0:
                            betting=False
                            
            P2BetAmountTurn=P2BetAmount
            AIturn=not AIturn
            while betting==True: #while one player can still bet
                if AIturn==True:
                    AIBetAmount = chooseCallRaiseOrFoldTurn(P2BetAmount)
                    if AIBetAmount==-1: #if the AI folds
                        betting=False
                        fold=True
                    elif AIBetAmount==0: #if AI calls
                        betting=False
                else:
                    P2BetAmount = requestBetCheckOrFold(AIBetAmount)
                    if P2BetAmount==-1: #if P2 folds
                        betting=False
                        fold=True
                    elif P2BetAmount==0:
                        betting=False
                AIturn=not AIturn
            
            P2BetAmountTurn=P2BetAmount
            
        """The River"""    
        if fold==False:
            River=requestRiver()
            betting=True
        
            #if AI bets first, request an action from the AI, if the AI checks then request a bet from P2
            if AIturn==True:
                AIBetAmount = chooseBetCheckOrFoldRiver() #must be implemented
                if AIBetAmount==-1: #if the AI folds
                    betting=False
                    fold=True
                elif AIBetAmount==0:
                    AIturn=not AIturn
                    P2BetAmount=requestBetCheckOrFold()
                    if P2BetAmount==-1: #if P2 folds
                        betting=False
                        fold=True
                    elif P2BetAmount==0:
                        betting=False
            #if P2 bets first, request an action from P2, if P2 checks then request a bet from the AI                
            else:
                P2BetAmount = requestBetCheckOrFold()
                if P2BetAmount==-1: #if P2 folds
                    betting=False
                    fold=True
                elif P2BetAmount==0:
                    AIturn=not AIturn
                    AIBetAmount = chooseBetCheckOrFoldRiver()
                    if AIBetAmount==-1: #if the AI folds
                        betting=False
                        fold=True
                    elif AIbetAmount==0:
                            betting=False

            
            P2BetAmountRiver=P2BetAmount #for data gathering
                            
            AIturn=not AIturn
            while betting==True: #while one player can still bet
                if AIturn==True:
                    AIBetAmount = chooseCallRaiseOrFoldRiver(P2BetAmount)
                    if AIBetAmount==-1: #if the AI folds
                        betting=False
                        fold=True
                    elif AIBetAmount==0: #if AI calls
                        betting=False
                else:
                    P2BetAmount = requestBetCheckOrFold(AIBetAmount)
                    if P2BetAmount==-1: #if P2 folds
                        betting=False
                        fold=True
                    elif P2BetAmount==0:
                        betting=False
                AIturn=not AIturn
            
            
            
            winner, P2Hand = declareWinner(fold)#need to write #requests player 2s cards and finds the winner
            allocatePot() #need to write
            if P2Hand!=Null:
                CurrentGameHistoryHole.append(gatherDataHole())  #[starting cards, how good were they, who went first, #how much did P2 bet, P2money]
                #CurrentHistoryFlop.append(gatherDataHole())
                #CurrentHistoryTurn.append(gatherDataHole())
                #CurrentHistoryRiver.append(gatherDataHole())
            
    #end of game
    
    if AImoney > 0:
        print("I took all of your money. Have a nice day")
    else:
        print("It appears that I have lost. That sucks")
    
        
if __name__ == '__main__':
    play()

