#!/usr/bin/python
# -*- coding: utf-8 -*-

class Player():
    
    def __init__(self,width):
        self.posx = width/2
        self.posy = 150
        self.speed = -10
        
    def drawPlayer(self):
        translate(self.posx, self.posy)
        rect(-12,-12,24,24)
        translate(-self.posx, -self.posy)
        
    def runPlayer(self, gameSpeed, dir):
        self.speed += 0.5
        self.posy += self.speed
        deltax = 1.0/gameSpeed*width
        if dir == 0:
            deltax = -deltax
        self.posx += deltax
        self.drawPlayer()
        
    def click(self):
        self.speed = -10
