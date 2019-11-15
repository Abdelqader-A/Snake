import random, os
path = os.getcwd()

class Game:
    def __init__(self,h,w):
        self.h = h
        self.w = w
        
    def show(self):

play = Game(720,1280)

def setup():
    background(#CDCDCD)
    size(game.w, game.h)
    
def draw():
    background(#CDCDCD)
    play.show()
    
