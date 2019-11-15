import random, os
path = os.getcwd()

class Game:
    def __init__(self,h,w):
        self.h = h
        self.w = w
        self.element = Element(300,300,30)
        
    def show(self):
        stroke(205,205,205)
        fill(205,205,205)
        noFill()
        stroke(0)
        self.element.show()
        
class Element:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
    
    def show(self):
        circle(self.x, self.y, self.d)

play = Game(600,600)

def setup():
    size(play.w, play.h)
    background(205,205,205)
    
    
def draw():
    background(205,205,205)
    play.show()
    
