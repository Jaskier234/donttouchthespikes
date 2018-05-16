#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint
from Player import Player

class Game():
    
    def __init__(self,width):
        self.spikes = []
        self.spikesCoordinates = []
        self.speed = 90 # aktualna prędkość gry
        self.currSpeed = self.speed/2 # ile zostało do zmiany kolców
        self.side = 0
        self.player = Player(width)
        self.gobuff = 10 # bufor kolizji z kolcem
        self.spikesSpacing = 45
        self.spikesFromTop = 20
        self.spikesFromBottom = 550
        self.spikeSize = 20 # promień
        self.genSpikes(3)
        
    def genSpikes(self,ile):
        self.spikes = []
        for i in range(ile):
            self.spikes.append(1)
        for i in range(11-ile):
            self.spikes.append(0)
            
        for i in range(22):
            a = randint(0,10)
            b = randint(0,10)
            self.spikes[a], self.spikes[b] = self.spikes[b], self.spikes[a]
        self.spikesCoordinates = []
        for i in zip(self.spikes,range(self.spikesFromTop+25,656,self.spikesSpacing)):
            if i[0] == 1:
                self.spikesCoordinates.extend(range(i[1]-self.spikeSize, i[1]+self.spikeSize))
            
    def isGameover(self):
        if self.player.posy > self.spikesFromBottom-12 or self.player.posy < self.spikesFromTop+12:
            return True
        if abs(self.player.posx - self.side) < self.gobuff:
            if int(self.player.posy) in self.spikesCoordinates:
                return True
        return False
    
    def drawSpikes(self):
        for i in zip(self.spikes,range(self.spikesFromTop+25,height,self.spikesSpacing)):
            if i[0]==1:
                translate(self.side, i[1])
                rotate(PI/4.0)
                rect(-12, -12, 25, 25)
                rotate(-PI/4.0)
                translate(-self.side, -i[1])
                
        rect(0,0,width,20)
        for i in range(25, width, self.spikesSpacing):
            translate(i,self.spikesFromTop)
            rotate(PI/4.0)
            rect(-12, -12, 25, 25)
            rotate(-PI/4.0)
            translate(-i,-self.spikesFromTop)
            
        rect(0,self.spikesFromBottom,width,height)
        for i in range(25, width, self.spikesSpacing):
            translate(i,self.spikesFromBottom)
            rotate(PI/4.0)
            rect(-12, -12, 25, 25)
            rotate(-PI/4.0)
            translate(-i,-self.spikesFromBottom)
        
    def runFrame(self):
        if self.isGameover():
            delay(1000)
            self.__init__(width)
        self.player.runPlayer(self.speed, self.side)
        self.currSpeed -= 1
        if self.currSpeed == 0:
            if self.side == 0:
                self.side = width
            else:
                self.side = 0
            self.currSpeed = self.speed
            self.genSpikes(3)
            
        self.drawSpikes()
        
