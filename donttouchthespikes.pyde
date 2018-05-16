import Game
import random

global a 
a = Game.Game(368)

def setup():
    size(368,656)
    #frameRate(20)
    background(200,200,200)
    noStroke()
    fill(50,50,50)
    
    a.drawSpikes()
    
def draw():
    background(200,200,200)
    a.runFrame()
    
def mousePressed():
    a.player.click()
            
