#encoding: utf8

'''
 Bárbara Jael (73241)
 Catarina Fonseca (75719)
 Miriam Cardoso (72181)
'''

from player import Player
from card import value
from data import *
import random

class StudentPlayer(Player):
    def __init__(self, name="Meu nome", money=0):
        super(StudentPlayer, self).__init__(name, money)

        # initialization of variables
        self.isFirst = True     # is first play in game
        self.rules = None
        self.startMoney = money
        self.amountBet = 0
        self.playType = 'h'		# type of play: hit (h), stand (s) or double (d)
        self.pointsMe = 0		# my initial points
        self.pointsDealer = 0	# dealer's initial points
        self.showHands = []
        
        # from data.py
        self.learntData = Data()
        self.learntData.readData()


    # --------------------------------------------------------------
    # the ones from "MANDATORY to re-implement all the next methods"
    # --------------------------------------------------------------

    def play(self, dealer, players):
        tmp = [d for d in players if d.player.name == self.name]	# from all the players, select me
        handMe = tmp[0].hand 		# my hand (in an array form)
        handDealer = dealer.hand 	# dealer's hand (in an array form)
        self.pointsMe = value(handMe)
        self.pointsDealer = value(handDealer)
        double = False
        

        # random
        #cmd = ['h', 's', 'u', 'd']
        #self.playType = cmd[random.randint(0,3)]

        
        # -- DOUBLE logic --
        # (only possible on the first hand)

        if self.isFirst:
            if self.pointsMe == 11 and hasAce(handDealer):
                double = True

        if double and self.isFirst:
            self.playType = 'd'
            self.isFirst = False
            return self.playType

        # -- force to HIT --

        # Always hit on 11 or less
        if self.pointsMe <= 11:
            self.playType = 'h'
        

        # update the odds to create a list of options
        H = self.learntData.data[self.pointsMe][self.pointsDealer].hit
        S = self.learntData.data[self.pointsMe][self.pointsDealer].stand
        U = self.learntData.data[self.pointsMe][self.pointsDealer].surrender
        options = {H: 'h', S: 's', U: 'u'}

        # pick the maximum value
        maxValue = max(options.keys())
        self.playType = options.get(maxValue)


        self.isFirst = False
        return self.playType


    def bet(self, dealer, players):
    	# estimates the winning factor (determines porpotion between current money and start money)
        factor = self.pocket / float(self.startMoney)
        
        # based on the winning factor, choose how much to bet
        if factor >= 2:
            amount = self.pocket / 30.0
        elif factor >= 1.5:
            amount = self.pocket / 60.0
        else:
            amount = self.pocket / 100.0

        # make sure the amount bet is within the rules' limits
        if amount > self.rules.max_bet:
            amount = self.rules.max_bet
        elif amount < self.rules.min_bet:
            amount = self.rules.min_bet

        self.amountBet = int(amount)
        return int(amount)



    # -----------------------------------------------------------
    # the ones from "MIGHT want to re-implement the next methods"
    # -----------------------------------------------------------
    
    def show(self, players):
        # update cards before payback
        tmp = [d for d in players[1:] if d.player.name == self.name]
        handMe = tmp[0].hand
        handDealer = players[0].hand
        self.showHands += [value(handMe), value(handDealer)]

    def want_to_play(self, rules):
        self.rules = rules
        return True
    

    # ------------------------------------------


    '''
     receives:
        - winner: bet + premium
        - loser: -bet
        - draw: 0
    '''
    def payback(self, prize):
        super(StudentPlayer, self).payback(prize)
        reward = 0

        # winner
        if prize > 0:
            reward = self.amountBet + 250

        # loser
        elif prize < 0:
            reward = - self.amountBet - 500

        # draw
        else:
            reward = 0
        

        #-------------------------

        # update rewards
        if self.playType == 'h':
            self.learntData.data[self.pointsMe][self.pointsDealer].hit += int(reward)   # force to be int because of previous problems on the matrix
        elif self.playType == 's':
            self.learntData.data[self.pointsMe][self.pointsDealer].stand += int(reward)
        elif self.playType == 'u':
            self.learntData.data[self.pointsMe][self.pointsDealer].surrender += int(reward)
        
        
        # other updates
        self.learntData.writeData()
        self.showHands = []
        self.isFirst = True


# ---------------------
#     other methods
# ---------------------
    
# checks if hand has ace - returns true if has
def hasAce(hand):
    v = ([c.is_ace() for c in hand])
    l = [x for x in v if x]
    if len(l) > 0:
        return True
    return False
